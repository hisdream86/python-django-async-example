from django.contrib import admin
from product import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    list_display_links = ("id",)
