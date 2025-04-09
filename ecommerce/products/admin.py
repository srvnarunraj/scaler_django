from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.site_header = "E-commerce Admin"
admin.site.site_title = "E-commerce Admin Login"
admin.site.index_title = "Welcome to the E-commerce Admin Portal"
admin.site.register(Product)