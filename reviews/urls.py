from django.urls import path
from .views import *

urlpatterns = [
    path("add/<int:product_id>/", add_review, name="add_review"),
]