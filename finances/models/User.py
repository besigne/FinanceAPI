from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    email = models.EmailField(blank=True, max_length=254, verbose_name='endereço de email', unique=True,
                              error_messages={'unique': 'Já existe um usuário cadastrado com esse e-mail.'})
    fixed_income = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(1000000)]
    )
    fixed_spending = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(1000000)]
    )

    class Meta:
        db_table = "user"
