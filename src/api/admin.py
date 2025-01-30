from django.contrib import admin
from src.api.models import Category, Product, Order
from src.api.models.feedback import Feedback


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
    ordering = ("-status",)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
