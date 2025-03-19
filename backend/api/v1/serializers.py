from rest_framework import serializers

import backend.api.v1.models as api_models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Category
        fields = ["id", "name", "product_count", "image"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Product
        fields = ["id", "name", "description", "price", "category", "image"]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Feedback
        fields = ["id", "name", "phone", "email", "message", "created_at"]


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = api_models.News
        fields = [
            "id",
            "category",
            "title",
            "image",
            "description_1",
            "description_2",
            "author",
            "created_at",
            "updated_at",
        ]


class FaireSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = api_models.Faire
        fields = [
            "id",
            "category",
            "title",
            "image",
            "description_1",
            "description_2",
            "author",
            "created_at",
            "updated_at",
        ]
