from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category']
        labels = {
            'name': 'Наименование товара',
            'description': 'Описание товара',
            'image': 'Фото товара'
        }


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=20,
        required=False,
        label='Найти'
    )
