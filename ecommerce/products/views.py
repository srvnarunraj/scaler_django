from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
def get_all_products(request):
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