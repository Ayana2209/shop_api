from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer


@api_view(["GET"])
def category_list_api_view(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.all(id=category_id)
    except Product.DoesNotExist:
        return Response(data={'error': "Category NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def product_derail_api_view(request, product_id):
    try:
        product = Product.objects.all(id=product_id)
    except Product.DoesNotExist:
        return Response(data={'error': "Product NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)


@api_view(["GET"])
def review_list_api_view(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.all(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'error': "Review NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)
