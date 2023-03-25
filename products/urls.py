from django.urls import path

from products.views.base import IndexView
from products.views.product import ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from products.views.review import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_add_view'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update_view'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('product/review/<int:pk>/add', ReviewCreateView.as_view(), name='review_add_view'),
    path('product/<int:pk>/review/edit', ReviewUpdateView.as_view(), name='review_update_view'),
    path('prdouct/review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete_view')
]
