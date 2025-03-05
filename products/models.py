from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Бренд')
    description = models.TextField(blank=True, null=True, verbose_name='Опис Бренду')
    website = models.URLField(max_length=200, blank=True, null=True, verbose_name='Сайт бренду')
    image = models.ImageField(upload_to='image/vendor_image/', null=True, blank=True, verbose_name='Файл зображення')
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Категорія')
    description = models.TextField(blank=True, null=True, verbose_name='Опис категорії')
    image = models.ImageField(upload_to='image/category_image/', null=True, blank=True, verbose_name='Файл зображення')
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тег')
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Жанр')
    image = models.ImageField(upload_to='image/genre_image/', null=True, blank=True, verbose_name='Файл зображення')
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'

    def __str__(self):
        return self.name

class Availability(models.TextChoices):
    IN_AVAILABILITY = "In availability", "В наявності"
    NOT_IN_AVAILABILITY = "Not in availability", "Немає в наявності"      

    
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Товар')
    code = models.CharField(max_length=50, unique=True, verbose_name='Артикул')  
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Акційна ціна')  
    note = models.TextField(blank=True, null=True, verbose_name='Нотатки')  
    tags = models.ManyToManyField('Tag', related_name='products', blank=True, verbose_name='Теги')
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, blank=True, null=True, related_name='products', verbose_name='Бренд')  
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='products', verbose_name='Категорія')
    genre = models.ManyToManyField('Genre', related_name='products', blank=True, verbose_name='Жанри')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створений') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлений') 
    availability = models.CharField(max_length=20, default=Availability.IN_AVAILABILITY, choices=Availability.choices, verbose_name="Наявність")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def clean(self):
        """Перевіряє, що акційна ціна не перевищує основну."""
        if self.sale_price and self.sale_price >= self.price:
            raise ValidationError({'sale_price': 'Акційна ціна повинна бути меншою за основну!'})

    def get_final_price(self):
        """Повертає акційну ціну, якщо є, інакше стандартну."""
        return self.sale_price if self.sale_price else self.price

    def __str__(self):
        category_name = self.product_category.name if self.product_category else "Без категорії"
        return f"{self.name} ({category_name})"
 

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = models.ImageField(upload_to='image/product_images/',verbose_name='Файл зображення')
    class Meta:
        verbose_name = 'Файл зображення'
        verbose_name_plural = 'Файли зображень'

    def __str__(self):
        return f"Image for {self.product.name}"




