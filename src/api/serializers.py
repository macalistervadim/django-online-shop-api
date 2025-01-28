from rest_framework import serializers

import src.api.models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = src.api.models.Order
        fields = '__all__'
