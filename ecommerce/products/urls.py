from django.urls import path
from . import views


urlpatterns = [
    path('getFirst/',views.getFirst, name='getFirst'),
    path('allproducts/',views.get_products, name='all_products'),
    path('products/<int:id>/',views.get_product_by_id, name='get_product'),
    path('products_post/',views.post_product_by_id, name='get_product'),
]