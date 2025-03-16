from typing import Any

from rest_framework import serializers

import backend.api.v1.models as api_models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Cart
        fields = ["id", "product_id", "user"]
        read_only_fields = ["user"]

    def create(self, validated_data: Any) -> Any:
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Order
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Feedback
        fields = "__all__"
