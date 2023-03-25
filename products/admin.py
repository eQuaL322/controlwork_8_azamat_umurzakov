from django.contrib import admin

from products.models import Product, Review


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'image')
    list_filter = ('id', 'name', 'category')
    search_fields = ('name', 'description')
    fields = ('name', 'category', 'description', 'image')
    readonly_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'rating')
    list_filter = ('id', 'author', 'rating')
    search_fields = ('author', 'product', 'text')
    fields = ('author', 'product', 'text', 'rating')
    readonly_fields = ('id', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
