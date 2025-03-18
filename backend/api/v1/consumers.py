import json
from typing import Any

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from backend.api.v1.services.chat_service import ChatService
from backend.api.v1.services.message_service import MessageService

"""
TODO:
- !!!!!!!УБРАТЬ typeignore!!!!!!!!

- добавить фикстуры
- оформить под репозиторий
- пофиксить сеттинги
- ci/cd
"""


class AdminChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        self.user = self.scope.get("user")
        if not self.user or not self.user.is_staff:
            await self.close(code=4003)
            return
        await self.accept()
        chats = await database_sync_to_async(ChatService.get_chats)()
        await self.send(text_data=json.dumps({"chats": chats}))


class UserChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        self.user = self.scope.get("user")
        self.chat_id = self.scope["url_route"]["kwargs"].get("chat_id")

        if not self.user or not self.chat_id:
            await self.close(code=4001)
            return

        self.chat = await database_sync_to_async(ChatService.get_chat)(
            self.chat_id,
        )
        if not self.chat or (
            not self.user.is_staff
            and not await database_sync_to_async(ChatService.is_customer)(
                self.chat,
                self.user,
            )
        ):
            await self.close(code=4003)
            return

        self.room_group_name = f"chat_{self.chat_id}"
        await self.accept()
        history = await database_sync_to_async(
            MessageService.get_chat_history,
        )(self.chat)
        await self.send(text_data=json.dumps({"history": history}))
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

    async def disconnect(self, code: Any) -> None:
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(
        self,
        text_data: str | None = None,
        bytes_data: bytes | None = None,
    ) -> None:
        if not text_data:
            return
        try:
            data = json.loads(text_data)
            message_content = data.get("message")
            if not message_content:
                await self.send(
                    text_data=json.dumps(
                        {"error": "Пустое сообщение"},
                    ),  # TODO: fix
                )
                return
            message = await database_sync_to_async(
                MessageService.save_message,
            )(self.chat, self.user, message_content)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message_id": message.id,
                    "message": message.content,
                    "author": "Administrator"
                    if self.user.is_staff
                    else self.user.username,
                    "timestamp": message.created_at.isoformat(),
                },
            )
        except json.JSONDecodeError:
            await self.send(
                text_data=json.dumps({"error": "Некорректный JSON"}),
            )

    async def chat_message(self, event: Any) -> None:
        await self.send(text_data=json.dumps(event))
