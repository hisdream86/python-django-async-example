from django.db import models, transaction

from product.models.base import BaseModel
from django_example.contrib.errors import BadRequest


class ProductManager(models.Manager):
    def create_with_validation(self, **kwargs):
        name = kwargs.get("name")
        with transaction.atomic():
            if self.filter(name=name).first() is not None:
                raise BadRequest(f"Product name '{name}' alreay exists.")
            return self.create(**kwargs)


class Product(BaseModel):
    # Columns
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    # Manager
    objects = ProductManager()

    class Meta:
        db_table = "products"
