import ujson

from django.http import HttpRequest, JsonResponse
from product.models import Product
from product import serializers

from middlewares.views import AsyncAPIView
from asgiref.sync import sync_to_async


class ProductsView(AsyncAPIView):
    async def post(self, request: HttpRequest):
        data = ujson.loads(request.body)
        req = serializers.ProductCreateRequestSerializer(data=data)
        req.is_valid(raise_exception=True)
        product = await sync_to_async(Product.objects.create)(**req.data)
        return JsonResponse(data=serializers.ProductSerializer(product).data)


class ProductView(AsyncAPIView):
    async def get(self, request: HttpRequest, pk: int):
        product = await sync_to_async(Product.objects.get)(id=pk)
        serializer = serializers.ProductSerializer(product)
        return JsonResponse(data=serializer.data)
