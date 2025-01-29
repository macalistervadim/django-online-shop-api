from django.urls import path, include
from rest_framework.routers import DefaultRouter

import src.api.views as views


router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"products", views.ProductViewSet)
router.register(r"orders", views.OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.LoginView.as_view(), name="login"),
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
