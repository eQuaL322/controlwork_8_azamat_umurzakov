from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product


class Review(models.Model):
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
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=1,
        verbose_name='Оценка',
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.author} = {self.product.name}'
