from rest_framework import serializers

from .models import Category, Product, Variation


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = [
            "title",
            "price",
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    variation_set = VariationSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "image",
            "variation_set",
        ]

    def get_image(self, obj):
        try:
            return obj.productimage_set.first().image.url
        except AttributeError:
            return None


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product:detail', lookup_field='slug')

    class Meta:
        model = Product
        fields = [
            "url",
            "title",
            "description",
        ]


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product:category-detail', lookup_field='slug')

    product_set = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "url",
            "title",
            "description",
            "product_set",  # obj.product_set.all()
            # "default_category",
        ]
