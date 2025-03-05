from django import forms
from .models import DeliveryMethod, PaymentMethod


class OrderForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        label="Ім'я",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Введіть ім'я"})
    )

    last_name = forms.CharField(
        max_length=50,
        required=True,
        label="Прізвище",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Введіть прізвище"})
    )

    phone_number = forms.CharField(
        max_length=20,
        required=True,
        label="Телефон",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Введіть номер телефону"})
    )

    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Введіть email"})
    )

    delivery_method = forms.ModelChoiceField(
        queryset=DeliveryMethod.objects.filter(is_active=True),
        label="Спосіб доставки",
        empty_label="Оберіть спосіб доставки",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    city_address = forms.CharField(
        max_length=100,
        required=True,
        label="Місто/Село",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть місто/село'})
    )

    delivery_address = forms.CharField(
        max_length=255,
        required=True,
        label="Адреса доставки",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть адресу доставки'})
    )

    payment_method = forms.ModelChoiceField(
        queryset=PaymentMethod.objects.filter(is_active=True),
        label="Спосіб оплати",
        empty_label="Оберіть спосіб оплати",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
