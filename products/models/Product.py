from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Product(models.Model):
    CATEGORIES = (
        ('books', 'books'),
        ('food', 'food'),
        ('other', 'other'),
        ('electronics', 'electronics')
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
        null=False,
        validators=[
            MinLengthValidator(limit_value=3),
            MaxLengthValidator(limit_value=100),
        ]
    )
    category = models.CharField(
        max_length=15,
        choices=CATEGORIES,
        default='other',
        verbose_name='Категория',
        null=False
    )
    description = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name='Описание'
    )
    image = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name="Фото товара"
    )

    def __str__(self):
        return self.name
