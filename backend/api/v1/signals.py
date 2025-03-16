from typing import Any

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from backend.api.v1.models import Product


@receiver(post_save, sender=Product)
def update_product_count_on_save(
    sender: Any,
    instance: Any,
    **kwargs: dict[str, Any],
) -> None:
    category = instance.category
    category.product_count = category.products.count()
    category.save()


@receiver(post_delete, sender=Product)
def update_product_count_on_delete(
    sender: Any,
    instance: Any,
    **kwargs: dict[str, Any],
) -> None:
    category = instance.category
    category.product_count = category.products.count()
    category.save()
