from django.contrib import admin
from django.utils.html import format_html
from .models import OrderStatus, DeliveryMethod, Order, Cart, PaymentMethod
from cart.models import CartItem
from products.models import Product

# 🔹 Способы доставки
@admin.register(DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('name',)

# 🔹 Способы оплаты
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('name',)

# 🔹 Товары в корзине (Inline для Cart)
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'get_price', 'get_total_price')

    def get_price(self, obj):
        return f"{obj.product.get_final_price()} грн"
    get_price.short_description = "Цена за единицу"

    def get_total_price(self, obj):
        return f"{obj.get_total_price()} грн"
    get_total_price.short_description = "Общая цена"

# 🔹 Кошик (чтобы видеть товары)
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_id', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'session_id')
    readonly_fields = ('created_at',)
    inlines = [CartItemInline]

# 🔹 Заказы
# 🔹 Заказы
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number", "user", "first_name", "last_name", "phone_number", "email",
        "city_address", "delivery_address", "status", "total_price", "created_at", "view_cart_items"
    )
    list_filter = ("status", "created_at", "delivery_method", "payment_method")
    search_fields = ("order_number", "user__username", "user__email", "first_name", "last_name", "phone_number", "email")
    readonly_fields = ('uuid', 'order_number', 'created_at', 'total_price')
    list_editable = ('status', "city_address", "delivery_address", "first_name", "last_name", "phone_number", "email")

    def view_cart_items(self, obj):
        if obj.cart:
            items = obj.cart.items.all()
            return format_html("<br>".join([f"{item.product.name} (x{item.quantity})" for item in items]))
        return "—"
    view_cart_items.short_description = "Товары в заказе"


# 🔹 Товары в корзине (отдельно)
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")

