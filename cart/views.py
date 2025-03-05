from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import *
from products.models import *
# Create your views here.

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart

def add_to_cart(request, product_id):
    """ Додає товар у корзину """
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    
    return JsonResponse({"message": "Товар додано в корзину", "cart_items": cart.items.count()}, json_dumps_params={'ensure_ascii': False})

def cart_detail(request):
    """ Відображає сторінку корзини """
    cart = get_or_create_cart(request)
    if cart.user and cart.user != request.user:
        return redirect("main_page")  
    context = {
        "cart": cart
        }
    return render(request, "cart/cart.html", context )

def action_cart(request, action_cart, product_id):
    cart = get_or_create_cart(request)
    cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()

    if not cart_item:
        return redirect("cart_detail")

    if action_cart == "remove":
        cart_item.delete()  

    elif action_cart == "decrease":
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    elif action_cart == "increase":
        if cart_item.quantity < 50:
            cart_item.quantity += 1
            cart_item.save()
        else:
            return JsonResponse({"message": "Додана дуже велика кількість товару"}, json_dumps_params={'ensure_ascii': False})

    return redirect("cart_detail")

def cart_count(request):
    cart = Cart.get_cart(request)
    return JsonResponse({"cart_items_count": cart.items.count() if cart else 0}) 

