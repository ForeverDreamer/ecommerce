from rest_framework import generics, filters
# from django_filters.rest_framework import DjangoFilterBackend


from .pagination import CategoryPagination
from .models import Product, Category
from .filters import ProductFilter
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductDetailSerializer
)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        # DjangoFilterBackend
    ]
    search_fields = ["title", "description"]
    ordering_fields = ["title", "id"]
    filter_class = ProductFilter


class ProductRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
