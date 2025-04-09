from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
def get_all_products(request):
    data = Product.objects.first()
    print(data.name)
    return HttpResponse(data.name)