from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, \
ProductSerializerReview, CategoryValidateSerializer, ProductValidateSerializer, ReviewValidateSerializer


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        # Step 1. Get data from body request
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        # Step 2. Create Category with data
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'message': 'Request failed',
                                  'error': serializer.errors})
        name = serializer.validated_data.get("name")
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
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={serializer.errors})
        category.name = serializer.validated_data.get("name")
        category.save()
        return Response(data=CategorySerializer(category).data)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={serializer.errors})
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description")
        price = serializer.validated_data.get("price")
        category_id = serializer.validated_data.get("category_id")
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
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={serializer.errors})
        product.title = serializer.validated_data.get("title")
        product.description = serializer.validated_data.get("description")
        product.price = serializer.validated_data.get("price")
        product.category_id = serializer.validated_data.get("category_id")
        product.save()
        return Response(data=ProductSerializer(product).data)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer()
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={serializer.errors})
        text = serializer.validated_data.get("text")
        stars = serializer.validated_data.get("stars")
        product_id = serializer.validated_data.get("product_id")
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
        serializer = ReviewValidateSerializer()
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={serializer.errors})
        review.text = serializer.validated_data.get("text")
        review.product_id = serializer.validated_data.get("product_id")
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)


@api_view(['GET'])
def product_review_list(request):
    product_review = Product.objects.all()
    serializer = ProductSerializerReview(product_review, many=True)
    return Response(data=serializer.data)