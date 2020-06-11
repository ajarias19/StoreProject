from django.contrib import admin

from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount', 'price')
    list_display_links = ('name',)
    list_filter = ('category',)
    search_fields = ('name', 'category')
    list_per_page = 25

admin.site.register(Product, ProductAdmin)
