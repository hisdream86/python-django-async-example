import ujson

from asgiref.sync import sync_to_async
from django.http import HttpRequest
from product.models import Product
from product import serializers

from django_example.contrib.views import AsyncAPIView
from django_example.contrib.response import APIResponse


class ProductsView(AsyncAPIView):
    async def post(self, request: HttpRequest):
        data = ujson.loads(request.body)
        req = serializers.ProductCreateRequestSerializer(data=data)
        req.is_valid(raise_exception=True)
        product = await sync_to_async(Product.objects.create_with_validation)(**req.data)
        return APIResponse(data=serializers.ProductSerializer(product).data)


class ProductView(AsyncAPIView):
    async def get(self, request: HttpRequest, pk: int):
        product = await sync_to_async(Product.objects.get)(id=pk)
        serializer = serializers.ProductSerializer(product)
        return APIResponse(data=serializer.data)
