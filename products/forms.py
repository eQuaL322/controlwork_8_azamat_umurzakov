from django import forms

from products.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category']
        labels = {
            'name': 'Наименование товара',
            'description': 'Описание товара',
            'image': 'Фото товара'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        labels = {
            'text': 'Текст',
            'rating': 'Оценка'
        }


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=20,
        required=False,
        label='Найти'
    )
