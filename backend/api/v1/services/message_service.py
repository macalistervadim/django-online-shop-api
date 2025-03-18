from typing import Any

from backend.api.v1.models import Chat, Message


class MessageService:
    @staticmethod
    def save_message(chat: Chat, user: Any, content: str) -> Message:
        return Message.objects.create(chat=chat, user=user, content=content)

    @staticmethod
    def get_chat_history(chat: Chat) -> list[dict]:
        messages = (
            Message.objects.filter(chat=chat)
            .select_related("user")
            .order_by("created_at")
        )
        return [
            {
                "message_id": msg.id,
                "content": msg.content,
                "author": "Administrator"
                if msg.user.is_staff
                else msg.user.username,
                "timestamp": msg.created_at.isoformat(),
            }
            for msg in messages
        ]
