from typing import Any

from django.db.models import QuerySet
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

import backend.api.v1.models as api_models
import backend.api.v1.serializers as api_serializers


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = api_models.Category.objects.all()
    serializer_class = api_serializers.CategorySerializer
    permission_classes = [permissions.AllowAny]


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = api_models.News.objects.all()
    serializer_class = api_serializers.NewsSerializer
    permission_classes = [permissions.AllowAny]


class FaireViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = api_models.Faire.objects.all()
    serializer_class = api_serializers.FaireSerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = api_models.Product.objects.all()
    serializer_class = api_serializers.ProductSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    @action(
        detail=True,
        methods=["post"],
        url_path="chat",
        permission_classes=[IsAuthenticated],
    )
    def chat(self, request: Request, pk: int | None = None) -> Response:
        """
        При вызове этого экшена (POST /products/<pk>/chat/) возвращается
        чат для продукта.
        Если чат ещё не создан – он создаётся.
        """
        product = self.get_object()

        # Проверка, что у пользователя есть ID, и передаем его
        customer_id = (
            request.user.id if request.user.is_authenticated else None
        )

        if customer_id is None:
            return Response(
                {"error": "User must be authenticated to create a chat."},
                status=400,
            )

        chat, created = api_models.Chat.objects.get_or_create(
            product=product,
            customer_id=customer_id,  # Передаем customer_id
        )

        return Response(
            {
                "chat_id": chat.id,
                "created": created,
            },
        )


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = api_models.Feedback.objects.all()
    serializer_class = api_serializers.FeedbackSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post"]

    def create(self, request: Request) -> Response:
        serializer = api_serializers.FeedbackSerializer(
            data=request.data,
            context={"request": request},
        )
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response(
            {"message": "Feedback created"},
            status=status.HTTP_201_CREATED,
        )


class FavoritesViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = api_models.Favorites.objects.all()
    serializer_class = api_serializers.FavoritesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        return api_models.Favorites.objects.filter(user=self.request.user)

    def create(
        self,
        request: Request,
        *args: Any,
        **kwargs: Any,
    ) -> Response:
        product_id = request.data.get("product")
        if not product_id:
            return Response(
                {"error": "Product ID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        favorite_exists = api_models.Favorites.objects.filter(
            user=request.user,
            product_id=product_id,
        ).exists()
        if favorite_exists:
            return Response(
                {"detail": "Product already in favorites."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        favorite = api_models.Favorites.objects.create(
            user=request.user,
            product_id=product_id,
        )
        serializer = self.get_serializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {
                    "error": "You do not have permission to "
                    "delete this favorite.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
