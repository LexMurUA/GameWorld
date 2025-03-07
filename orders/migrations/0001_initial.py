# Generated by Django 4.2.18 on 2025-02-21 15:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Спосіб доставки')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Вартість')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активний')),
            ],
            options={
                'verbose_name': 'Спосіб доставки',
                'verbose_name_plural': 'Способи доставки',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Загальна сума')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('status', models.CharField(choices=[('new', 'Нове'), ('processing', 'В обробці'), ('shipped', 'Відправлено'), ('delivered', 'Доставлено'), ('cancelled', 'Скасовано')], default='new', max_length=20, verbose_name='Статус')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Кошик')),
                ('delivery_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.deliverymethod', verbose_name='Спосіб доставки')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
            },
        ),
    ]
