import json
from typing import Any

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from backend.api.v1.models import Chat, Message

"""
TODO:
- добавить очисту мессенджей раз в год
- добавить отправку истории сообщений с подключением
- добавить вывод последнего сообщений юзера в админке

- !!!!!!!УБРАТЬ typeignore!!!!!!!!

- пофиксить модельки
- добавить фикстуры
- оформить под репозиторий
- пофиксить сеттинги
- ci/cd
"""


class AdminChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        if "user" not in self.scope:
            await self.close(code=4001)
            return

        self.user = self.scope["user"]

        if not self.user.is_staff:
            await self.close(code=4003)
            return

        await self.accept()

        chats = await self.get_chats()

        await self.send(text_data=json.dumps({"chats": chats}))

    @database_sync_to_async
    def get_chats(self) -> list[dict[str, Any]]:
        return list(
            Chat.objects.select_related("customer", "product").values(  # type: ignore
                "id",
                "customer__username",
                "product__name",
            ),
        )


class UserChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        if "user" not in self.scope:
            await self.close(code=4001)
            return

        self.user = self.scope["user"]
        self.chat_id = self.scope["url_route"]["kwargs"].get("chat_id")

        if not self.chat_id:
            await self.close(code=4002)
            return

        self.chat = await self.get_chat(self.chat_id)
        if not self.chat:
            await self.close(code=4004)
            return

        if not self.user.is_staff and not await self.is_customer(self.chat):
            await self.close(code=4003)
            return

        self.room_group_name = f"chat_{self.chat_id}"

        await self.accept()

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

    @database_sync_to_async
    def get_chat(self, chat_id: int) -> Chat | None:
        try:
            return Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            return None

    @database_sync_to_async
    def is_customer(self, chat: Chat) -> bool:
        return self.user == chat.customer

    async def disconnect(self, code: int) -> None:
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(
        self,
        text_data: str | None = None,
        bytes_data: bytes | None = None,
    ) -> None:
        if text_data:
            try:
                text_data_json = json.loads(text_data)
                message_content = text_data_json.get("message")

                if not message_content:
                    await self.send(
                        text_data=json.dumps({"error": "Пустое сообщение"}),
                    )
                    return

                await self.save_message(message_content)

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        "type": "chat_message",
                        "message": message_content,
                    },
                )
            except json.JSONDecodeError:
                await self.send(
                    text_data=json.dumps({"error": "Некорректный JSON"}),
                )

    @database_sync_to_async
    def save_message(self, message_content: str) -> Message:
        return Message.objects.create(
            chat=self.chat,
            user=self.user,
            content=message_content,
        )

    async def chat_message(self, event: dict) -> None:
        await self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                },
            ),
        )
