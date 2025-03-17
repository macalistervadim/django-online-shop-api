from rest_framework import serializers

import backend.api.v1.models as api_models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Category
        fields = ["name", "product_count", "image"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Product
        fields = ["name", "description", "price", "category", "image"]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Feedback
        fields = ["name", "phone", "email", "message", "created_at"]
