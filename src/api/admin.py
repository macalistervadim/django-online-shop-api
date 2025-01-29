from django.contrib import admin
from src.api.models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "product_count")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
    )
    search_fields = ("name", "category__name")
    list_filter = ("category",)
    ordering = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "product__name", "order_date", "status")
    search_fields = ("user", "order_date", "status")
    list_filter = ("status",)
    ordering = ("status",)
