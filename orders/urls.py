from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('my-orders/', order_list, name='order_list'),
    path('order/<uuid:order_uuid>/', order_detail, name='order_detail'),
]
