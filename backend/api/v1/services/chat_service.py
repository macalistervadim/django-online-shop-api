from typing import Any

from backend.api.v1.models import Chat


class ChatService:
    @staticmethod
    def get_chats() -> list[dict[str, Any]]:
        chats = (
            Chat.objects.select_related("customer", "product")
            .prefetch_related("messages")
            .all()
        )
        result = []
        for chat in chats:
            last_message = chat.messages.order_by("-created_at").first()
            result.append(
                {
                    "id": chat.id,
                    "customer_username": chat.customer.username,
                    "product_name": chat.product.name
                    if chat.product
                    else None,
                    "last_message": last_message.content
                    if last_message
                    else "",
                    "last_message_time": last_message.created_at.isoformat()
                    if last_message
                    else None,
                },
            )
        return result

    @staticmethod
    def get_chat(chat_id: int) -> Chat | None:
        try:
            return Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            return None

    @staticmethod
    def is_customer(chat: Chat, user: Any) -> bool:
        return chat.customer == user
