from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    """Кастомний користувач із UUID замість ID та номером телефону"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    phone_number = models.CharField(
        max_length=15, 
        unique=True, 
        null=True, 
        blank=True, 
        verbose_name="Номер телефону"
    )

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users_groups",
        blank=True,
        help_text="Групи, до яких належить цей користувач.",
        verbose_name="Групи"
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",
        blank=True,
        help_text="Специфічні дозволи користувача.",
        verbose_name="Дозволи"
    )

    def __str__(self):
        return self.username
