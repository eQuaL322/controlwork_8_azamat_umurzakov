from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import TextChoices

from products.models import Product


class CategoryChoice(TextChoices):
    ONE = '1', '1'
    TWO = '2', '2'
    THREE = '3', '3'
    FOUR = '4', '4'
    FIVE = '5', '5'


class Review(models.Model):
    # RATING = (
    #     ('one', '1'),
    #     ('two', '2'),
    #     ('three', '3'),
    #     ('four', '4'),
    #     ('five', '5')
    # )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='review',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        verbose_name='Продукт',
        to=Product,
        related_name='review',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        max_length=2000,
        verbose_name='Текст',
        null=False,
        blank=False
    )
    rating = models.CharField(
        choices=CategoryChoice.choices,
        default=CategoryChoice.ONE,
        verbose_name='Оценка',
        max_length=1
    )

    def __str__(self):
        return f'{self.author} = {self.product.name}'
