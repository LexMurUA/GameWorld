# Generated by Django 5.1.5 on 2025-02-24 11:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(choices=[('very_good', 'Дуже добре 👍'), ('good', 'Добре 😃'), ('not_bad', 'Непогано 👌'), ('not_enough', 'Недостатньо 😞'), ('very_bad', 'Дуже погано 😢')], max_length=20, verbose_name='Оцінка')),
                ('text', models.TextField(max_length=800, verbose_name='Текст відгуку')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментарі',
                'ordering': ['-created_at'],
            },
        ),
    ]
