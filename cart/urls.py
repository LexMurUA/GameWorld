from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path("cart/<str:action_cart>/<int:product_id>/", action_cart, name="action_cart"),
    path("count/", cart_count, name="cart_count"),
]