from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

import src.api.models as api_models
import src.api.serializers as api_serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = api_models.Category.objects.all()
    serializer_class = api_serializers.CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = api_models.Product.objects.all()
    serializer_class = api_serializers.ProductSerializer
    permission_classes = [permissions.AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    queryset = api_models.Cart.objects.all()
    serializer_class = api_serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request):
        product_id = request.data.get("product_id")
        if not product_id:
            return Response(
                {"error": "product_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            product = api_models.Product.objects.get(id=product_id)
        except api_models.Product.DoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        cart_item, created = api_models.Cart.objects.get_or_create(
            user=request.user, product_id=product,
        )
        if not created:
            return Response(
                {"message": "Product already in cart"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"message": "Product added to cart"},
            status=status.HTTP_201_CREATED,
        )

    def destroy(self, request, pk=None):
        try:
            cart_item = api_models.Cart.objects.get(user=request.user, id=pk)
        except api_models.Cart.DoesNotExist:
            return Response(
                {"error": "Cart item not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        cart_item.delete()
        return Response(
            {"message": "Cart item removed"},
            status=status.HTTP_204_NO_CONTENT,
        )


class OrderViewSet(viewsets.ModelViewSet):
    queryset = api_models.Order.objects.all()
    serializer_class = api_serializers.OrderSerializer
    http_method_names = ["get", "post"]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request):
        try:
            product_id = request.data.get("product_id")
            quantity = request.data.get("quantity")
            delivery_date = request.data.get("delivery_date")

            if not product_id or not quantity or not delivery_date:
                return Response(
                    {"error": "Missing required fields"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            product = api_models.Product.objects.get(id=product_id)
            api_models.Order.objects.create(
                user=request.user,
                product=product,
                quantity=quantity,
                delivery_date=delivery_date,
            )
            return Response(
                {"message": "Order created"}, status=status.HTTP_201_CREATED,
            )

        except ObjectDoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = api_models.Feedback.objects.all()
    serializer_class = api_serializers.FeedbackSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post"]

    def create(self, request):
        serializer = api_serializers.FeedbackSerializer(
            data=request.data, context={"request": request},
        )
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(
            {"message": "Feedback created"},
            status=status.HTTP_201_CREATED,
        )
