from django.db import models
from products.models import *
from django.conf import settings


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,verbose_name="Користувач")  
    session_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="Незареєстрований користувач")  
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата створення")
    is_active = models.BooleanField(default=True, verbose_name="Активно") 

    def deactivate(self):
        self.is_active = False
        self.save()

    @staticmethod
    def get_cart(request):
        from cart.views import get_or_create_cart 
        return get_or_create_cart(request)

    def __str__(self):
        return f"Cart {self.id} (User: {self.user}, Session: {self.session_id})"
    
    class Meta:
        verbose_name = "Кошик"
        verbose_name_plural = "Кошики"

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items", verbose_name="Кошик")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")

    class Meta:
        verbose_name = "Історія Кошиків"
        verbose_name_plural = "Історія Кошиків"
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Cart {self.cart.id})"

    def get_total_price(self):
        return self.quantity * self.product.get_final_price()  

    