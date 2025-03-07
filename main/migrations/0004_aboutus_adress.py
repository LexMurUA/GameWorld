# Generated by Django 5.1.5 on 2025-02-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_advertising_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_about', models.CharField(blank=True, max_length=500, null=True, verbose_name='Інформація про магазин')),
            ],
            options={
                'verbose_name': 'Інформація про магазин',
                'verbose_name_plural': 'Інформація про магазин',
            },
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Посилання на гугл карту')),
                ('adress_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адреса')),
            ],
            options={
                'verbose_name': 'Адреса магазину',
                'verbose_name_plural': 'Адреси магазину',
            },
        ),
    ]
