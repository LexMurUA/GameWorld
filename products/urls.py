from django.urls import path
from .views import *

urlpatterns = [
    path("search/", product_search, name="product_search"),
    path('<str:product_menu>/', product_menu, name='product_menu_page'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('vendor/<int:vendor_id>/', vendor_detail, name='vendor_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'), 
]