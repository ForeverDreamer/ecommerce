from django.urls import path

from .views import (
    ProductListAPIView,
    ProductRetrieveAPIView,
    CategoryListAPIView,
    CategoryRetrieveAPIView
)

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/<str:slug>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path('', ProductListAPIView.as_view(), name='list'),
    path('<str:slug>/', ProductRetrieveAPIView.as_view(), name='detail'),
]
