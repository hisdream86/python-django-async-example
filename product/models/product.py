from django.db import models
from uuid import uuid4

from product.models.base import BaseModel


class Product(BaseModel):
    product_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        db_table = "products"
