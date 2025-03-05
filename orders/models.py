import uuid
from django.db import models
from django.conf import settings
from cart.models import Cart

class OrderStatus(models.TextChoices):
    NEW = "new", "Нове"
    PROCESSING = "processing", "В обробці"
    SHIPPED = "shipped", "Відправлено"
    DELIVERED = "delivered", "Доставлено"
    CANCELLED = "cancelled", "Скасовано"

class DeliveryMethod(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Спосіб доставки")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Вартість")
    is_active = models.BooleanField(default=True, verbose_name="Активний")

    class Meta:
        verbose_name = "Спосіб доставки"
        verbose_name_plural = "Способи доставки"

    def __str__(self):
        return f"{self.name} ({self.price} грн)"

class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Спосіб оплати")
    is_active = models.BooleanField(default=True, verbose_name="Активний")

    class Meta:
        verbose_name = "Спосіб оплати"
        verbose_name_plural = "Способи оплати"

    def __str__(self):
        return self.name

class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    order_number = models.PositiveIntegerField(unique=True, editable=False, null=True, verbose_name="Номер замовлення")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Користувач")

    # Нові поля для замовлення
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Прізвище")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Кошик")

    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.SET_NULL, null=True, verbose_name="Спосіб доставки")
    city_address = models.CharField(max_length=100, blank=True, null=True, verbose_name="Місто/Село")
    delivery_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адреса доставки")
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, verbose_name="Спосіб оплати")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Загальна сума")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.NEW,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ['-created_at']

    def __str__(self):
        return f"Замовлення №{self.order_number or '---'} ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.all().order_by('-order_number').first()
            self.order_number = (last_order.order_number + 1) if last_order else 10001
        super().save(*args, **kwargs)
