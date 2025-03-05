from .models import Cart

def cart_context(request):
    cart = Cart.get_cart(request) 
    return {"cart_items_count": cart.items.count() if cart else 0}