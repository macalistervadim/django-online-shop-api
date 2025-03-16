from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "В ожидании"),
        ("paid", "Оплачено"),
        ("delivered", "Доставлено"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    def __str__(self) -> str:
        return f"{self.user.username}'s order - {self.product.name}"
