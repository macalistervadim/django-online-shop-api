from django.contrib.auth.models import User
from django.db import models

from backend.api.v1.models import Product


class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="favorited_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")
        verbose_name = "favorites"
        verbose_name_plural = "favorites"

    def __str__(self) -> str:
        return f"Favorites - {self.user}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"user={self.user!r}, "
            f"product={self.product!r}, "
            f"created_at={self.created_at!r})"
        )
