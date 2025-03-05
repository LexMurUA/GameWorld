from django.urls import path
from .views import *

urlpatterns = [
    path('',main, name='main_page'),
    path('about/', about_page, name='about_page'),
    path('contact/', contact_page, name='contact_page'),
    
]