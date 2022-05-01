from django.db import models

from product.models.base import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        db_table = "products"
