from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

# Create your views here.
def getFirst(request):
    data = Product.objects.first()
    print(data.name)
    # Edit the Data Object
    data.name = "Samsung Galaxy S21"
    data.save()
    # Fetch the Data Object (Works with first() - will all-> lazy loading)
    # data = Product.objects.all() # This will edit the data object
    data = Product.objects.first()
    print(data.name)
    return HttpResponse(data.name)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True)
    return Response(serialized_products.data)

@api_view(['GET'])
def get_product_by_id(request, id):
    try:
        # product = Product.objects.filter(id=id) # In implementation it can return an empty list also 
        product = Product.objects.get(id=id) # Will throw error if not found
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
    
    serialized_product = ProductSerializer(product)
    return Response(serialized_product.data)

@api_view(['POST'])
def post_product_by_id(request):
    product = Product.objects.get(id=request.data.get('id'))
    product.name = request.data.get('name' )
    product.price = request.data.get('price')
    product.save()
    serialized_product = ProductSerializer(product)
    return Response(serialized_product.data)