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