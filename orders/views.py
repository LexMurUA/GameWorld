from django.shortcuts import render, redirect, get_object_or_404
from cart.views import get_or_create_cart
from cart.models import Cart, CartItem
from .models import Order, DeliveryMethod
from django.contrib.auth.decorators import login_required
from .forms import OrderForm


def create_order(request):
    cart = get_or_create_cart(request)

    if not cart.items.exists():
        return redirect("cart_detail")  # Якщо корзина порожня

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            delivery_method = form.cleaned_data["delivery_method"]
            payment_method = form.cleaned_data["payment_method"]
            city_address = form.cleaned_data["city_address"]
            delivery_address = form.cleaned_data["delivery_address"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]

            total_price = sum(item.get_total_price() for item in cart.items.all()) + delivery_method.price

            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                cart=cart,
                delivery_method=delivery_method,
                payment_method=payment_method,
                city_address=city_address,
                delivery_address=delivery_address,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                total_price=total_price,
            )

            cart.is_active = False
            cart.save()  # ВАЖЛИВО! Це збереже кошик у базі даних
            request.session.pop("cart_id", None)

            if not request.user.is_authenticated:
                request.session["order_uuid"] = str(order.uuid)

            return redirect("order_detail", order_uuid=order.uuid)
    else:
        form = OrderForm()

    return render(request, "orders/create_order.html", {"cart": cart, "form": form})



def order_detail(request, order_uuid):
    """Перегляд замовлення за UUID"""
    order = get_object_or_404(Order, uuid=order_uuid)

    if order.user:
        # Перевірка для зареєстрованого користувача
        if request.user != order.user:
            return redirect("main_page")
    else:
        # Перевірка для незареєстрованого користувача
        if request.session.get("order_uuid") != str(order.uuid):
            return redirect("main_page")

    return render(request, "orders/order_detail.html", {"order": order})


@login_required
def order_list(request):
    """Список замовлень користувача"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "orders/order_list.html", {"orders": orders})
