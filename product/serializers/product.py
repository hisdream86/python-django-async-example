from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    price = serializers.IntegerField(required=True, allow_null=False)
