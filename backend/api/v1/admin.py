from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin
from unfold.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)

from backend.api.v1.models import Category, Product
from backend.api.v1.models.feedback import Feedback


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("name", "product_count")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
    )
    search_fields = ("name", "category__name")
    list_filter = ("category",)
    ordering = ("name",)


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
