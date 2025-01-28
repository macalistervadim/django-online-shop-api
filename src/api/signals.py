from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from src.api.models import Product


@receiver(post_save, sender=Product)
def update_product_count_on_save(sender, instance, **kwargs):
    category = instance.category
    category.product_count = category.products.count()
    category.save()


@receiver(post_delete, sender=Product)
def update_product_count_on_delete(sender, instance, **kwargs):
    category = instance.category
    category.product_count = category.products.count()
    category.save()