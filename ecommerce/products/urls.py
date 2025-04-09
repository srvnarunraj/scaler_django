from django.urls import path
from . import views


urlpatterns = [
    path('getAll/',views.get_all_products, name='get_all_products'),
]