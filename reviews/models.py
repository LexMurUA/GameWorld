from django.db import models
from django.conf import settings
from products.models import Product

class Mark(models.TextChoices):
    VERY_GOOD = "very_good", "Дуже добре 👍"
    GOOD = "good", "Добре 😃"
    NOT_BAD = "not_bad", "Непогано 👌"
    NOT_ENOUGH = "not_enough", "Недостатньо 😞"
    VERY_BAD = "very_bad", "Дуже погано 😢"

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", verbose_name="Товар")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Користувач")
    mark = models.CharField(max_length=20, choices=Mark.choices, verbose_name="Оцінка")
    text = models.TextField(max_length=800, verbose_name="Текст відгуку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ["-created_at"]  

    def __str__(self):
        return f"Відгук від {self.user.name} для {self.product} ({self.get_mark_display()})"

