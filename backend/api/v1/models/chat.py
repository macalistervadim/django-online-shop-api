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

    def __str__(self) -> str:
        return f"Chat with {self.customer.username} about {self.product.name}"


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        related_name="messages",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.content[:50]}"
