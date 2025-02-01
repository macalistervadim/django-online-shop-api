from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import src.api.views as views


router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet, basename="categories")
router.register(r"products", views.ProductViewSet, basename="products")
router.register(r"feedbacks", views.FeedbackViewSet, basename="feedbacks")
router.register(r"orders", views.OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        'cart/',
        views.CartViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='cart-list-create',
    ),
    path(
        'cart/<int:pk>/',
        views.CartViewSet.as_view({'delete': 'destroy'}),
        name='cart-delete',
    ),
]
