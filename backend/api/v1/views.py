from rest_framework import permissions, status, viewsets
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
    permission_classes = [permissions.AllowAny]


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
