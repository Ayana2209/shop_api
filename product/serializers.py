from rest_framework import serializers
from product.models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name product_count'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()


class ProductSerializerReview(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "id title description price category gpa_rating".split()


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=5, max_length=15)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=4, max_length=15)
    description = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.IntegerField()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=10)