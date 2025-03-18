from django.contrib.auth.models import User
from django.db import models

from backend.api.v1.models.product import Product


class Chat(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="chats",
        on_delete=models.CASCADE,
    )
    customer = models.ForeignKey(
        User,
        related_name="customer_chats",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "chat"
        verbose_name_plural = "chats"

    def __str__(self) -> str:
        return f"Chat with {self.customer.username} about {self.product.name}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"product={self.product!r}, "
            f"customer={self.customer!r}, "
            f"created_at={self.created_at!r}, "
            f"updated_at={self.updated_at!r})"
        )


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        related_name="messages",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"

    def __str__(self) -> str:
        return f"{self.user.username}: {self.content[:50]}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"chat={self.chat!r}, "
            f"user={self.user!r}, "
            f"content={self.content!r}, "
            f"created_at={self.created_at!r})"
        )
