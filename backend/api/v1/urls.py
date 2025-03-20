from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import backend.api.v1.routing as chat_routing
import backend.api.v1.views as views

router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet, basename="categories")
router.register(r"products", views.ProductViewSet, basename="products")
router.register(r"feedbacks", views.FeedbackViewSet, basename="feedbacks")
router.register(r"faire", views.FaireViewSet, basename="faire")
router.register(r"news", views.NewsViewSet, basename="news")
router.register(r"favorites", views.FavoritesViewSet, basename="favorites")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("chat/", include(chat_routing.websocket_urlpatterns)),
]
