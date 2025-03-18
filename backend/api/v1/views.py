from rest_framework import permissions, status, viewsets
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
        При вызове этого экшена (POST /v1/products/<pk>/chat/) возвращается
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
