from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from product.models import Product
from product import serializers


class ProductViewSet(ViewSet):
    """
    A ViewSet for implementing APIs to manage products.
    """

    def create(self, request: Request):
        req = serializers.ProductCreateRequestSerializer(data=request.data)
        req.is_valid(raise_exception=True)
        product = Product.objects.create(**req.data)
        return Response(data=serializers.ProductSerializer(product).data)

    def retrieve(self, request: Request, pk: int = None):
        product = Product.objects.get(id=pk)
        serializer = serializers.ProductSerializer(product)
        return Response(data=serializer.data)
