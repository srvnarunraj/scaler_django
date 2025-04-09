from django.urls import path
from . import views


urlpatterns = [
    path('getFirst/',views.getFirst, name='getFirst'),
    path('allproducts/',views.get_products, name='all_products'),
]