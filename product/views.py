from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, \
ProductSerializerReview


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        # Step 1. Get data from body request
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        # Step 2. Create Category with data

        name = request.data.get("name")
        category = Category.objects.create(name=name)
        # Step 3. Return response (status) as created object
        return Response(data=CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.all(id=category_id)
    except Product.DoesNotExist:
        return Response(data={'error': "Category NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        category.name = request.data.get("name")
        category.save()
        return Response(data=CategorySerializer(category).data)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")
        category_id = request.data.get("category_id")
        product = Product.objects.create(title=title, description=description, price=price, category_id=category_id)
        return Response(data=ProductSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_derail_api_view(request, product_id):
    try:
        product = Product.objects.all(id=product_id)
    except Product.DoesNotExist:
        return Response(data={'error': "Product NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        product.title = request.data.get("title")
        product.description = request.data.get("description")
        product.price = request.data.get("price")
        product.category_id = request.data.get("category_id")
        product.save()
        return Response(data=ProductSerializer(product).data)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get("text")
        stars = request.data.get("stars")
        product_id = request.data.get("product_id")
        reviews = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=ReviewSerializer(reviews).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.all(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'error': "Review NOT FOUND"},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        review.text = request.data.get("text")
        review.product_id = request.data.get("product_id")
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET'])
def product_review_list(request):
    product_review = Product.objects.all()
    serializer = ProductSerializerReview(product_review, many=True)
    return Response(data=serializer.data)