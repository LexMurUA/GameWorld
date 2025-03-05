from django.shortcuts import render
from .models import *
from django.http import request, response
from products import *
from products.models import ProductImage, Product

# Create your views here.
def main(request):
        images = ProductImage.objects.select_related('product').all()  
        banners = Advertising.objects.select_related('adv_image').all()
        context ={
             'images': images,
             'banners': banners
        }
        return render(request, 'main/index.html', context)

def about_page(request):
    about_us = AboutUs.objects.first() 
    context = {'about_us': about_us}
    return render(request, 'main/about_page.html', context)

def contact_page(request):
    adress = Adress.objects.first()      
    context = {
        'adress': adress,
    }
    return render(request, 'main/contact_page.html', context)

