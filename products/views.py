from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import request, response, HttpResponseNotFound

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Product, Vendor, Category

def product_menu(request, product_menu):
    vendor_id = request.GET.get("vendor")  
    category_id = request.GET.get("category")  

    if product_menu == "categories":
        items = Category.objects.all()
    elif product_menu == "vendors":
        items = Vendor.objects.all()
    elif product_menu == "products":
        items = Product.objects.all()

       
        if vendor_id:
            items = items.filter(vendor__id=vendor_id)
        if category_id:
            items = items.filter(product_category__id=category_id)
    else:
        items = None 

    context = {
        'items': items,
        'product_menu': product_menu,
        'categories': Category.objects.all(),  
        'vendors': Vendor.objects.all(),  
        'selected_vendor': vendor_id,
        'selected_category': category_id
    } 
    return render(request, 'products/product_menu.html', context)

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    context = {
        'vendor': vendor, 
        'products': vendor.products.all(),
        'availability_choices': Availability
        }
    return render(request, 'products/vendor_detail.html', context)

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    context = {
        'category': category, 
        'products': category.products.all(),
        'availability_choices': Availability
        }  
    return render(request, 'products/category_detail.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
        'availability_choices': Availability
    }
    return render(request, 'products/product_detail.html', context)


def product_search(request):
    query = request.GET.get("q", "").strip()
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query) | \
                  Product.objects.filter(description__icontains=query) | \
                  Product.objects.filter(code__icontains=query)

    return render(request, "products/product_search.html", {
        "query": query,
        "results": results
    })
