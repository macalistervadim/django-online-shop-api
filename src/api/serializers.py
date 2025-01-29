from rest_framework import serializers

import src.api.models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Cart
        fields = ["id", "product_id", "user"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Order
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
