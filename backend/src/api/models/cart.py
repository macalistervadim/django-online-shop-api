from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart",
    )
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name}"
