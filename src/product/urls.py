from django.urls import path
from .views import category_list, create_category, create_product, product_list

urlpatterns = [
    path('category-list/', category_list, name='category_list'),
    path('create-category/', create_category, name='create_category'),
    path('create-product/', create_product, name='create_product'),
    path('products-list/', product_list, name='products-list')
]
