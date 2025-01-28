from django.contrib import admin

import src.api.models 


@admin.register(src.api.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(src.api.models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass