from django.db import models

class Advertising(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва акції')
    link = models.URLField(blank=True, null=True, verbose_name='Посилання на акцію')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створений')  
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлений')  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акція'
        verbose_name_plural = 'Акції'


class AdvertisingImage(models.Model):
    advertising = models.OneToOneField(Advertising, on_delete=models.CASCADE, related_name='adv_image', verbose_name='Акція')
    image = models.ImageField(upload_to='image/advertising_images/', verbose_name='Рекламний банер')

    def __str__(self):
        return f"Image for {self.advertising.name}"

    class Meta:
        verbose_name = 'Зображення акції'
        verbose_name_plural = 'Зображення акцій'
        ordering = ['id']

from django.db import models

class Adress(models.Model):
    link = models.URLField(blank=True, null=True, verbose_name='Посилання на гугл карту')
    adress_text = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адреса')

    def __str__(self):
        return self.adress_text or "Невказана адреса"

    class Meta:
        verbose_name = 'Адреса магазину'
        verbose_name_plural = 'Адреси магазину'




class AboutUs(models.Model):
    text_about = models.CharField(max_length=500, blank=True, null=True, verbose_name='Інформація про магазин')

    def __str__(self):
        return self.text_about[:50] if self.text_about else "Інформація про магазин"

    class Meta:
        verbose_name = 'Інформація про магазин'
        verbose_name_plural = 'Інформація про магазин'
