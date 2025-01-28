import json

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from rest_framework.views import csrf_exempt

import src.api.models as api_models
import src.api.serializers as api_serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = api_models.Category.objects.all()
    serializer_class = api_serializers.CategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = api_models.Product.objects.all()
    serializer_class = api_serializers.ProductSerializer
    permission_classes = [permissions.AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    queryset = api_models.Cart.objects.all()
    serializer_class = api_serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def add(self, request):
        product_id = request.data.get('product_id')
        product = api_models.Product.objects.get(id=product_id)
        cart_item, created = api_models.Cart.objects.get_or_create(
            user=request.user, product=product)
        if not created:
            return Response(
                {'message': 'Product already in cart'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {'message': 'Product added to cart'},
            status=status.HTTP_201_CREATED,
        )

    @action(detail=True, methods=['delete'])
    def remove(self, request, pk=None):
        cart_item = self.get_object()
        cart_item.delete()
        return Response(
            {'message': 'Product removed from cart'},
            status=status.HTTP_204_NO_CONTENT,
        )


class OrderViewSet(viewsets.ModelViewSet):
    queryset = api_models.Order.objects.all()
    serializer_class = api_serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        delivery_date = request.data.get('delivery_date')
        product = api_models.Product.objects.get(id=product_id)
        order = api_models.Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            delivery_date=delivery_date
        )
        return Response(
            {'message': 'Order created'}, status=status.HTTP_201_CREATED)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            # Чтение JSON-данных из тела запроса
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                csrf_token = get_token(request)
                return JsonResponse({'csrfToken': csrf_token}, status=200)
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)