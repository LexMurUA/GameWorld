# Generated by Django 5.1.5 on 2025-02-27 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_is_active'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Кошик', 'verbose_name_plural': 'Кошики'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Історія Кошиків', 'verbose_name_plural': 'Історія Кошиків'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='session_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Незареєстрований користувач'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cart', verbose_name='Кошик'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Кількість'),
        ),
    ]
