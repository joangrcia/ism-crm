from django.contrib import admin
from .models import ProductTrading

# Register your models here.
@admin.register(ProductTrading)
class ProductTradingAdmin(admin.ModelAdmin):
    list_display = ('name', 'leverage', 'min_deposit', 'is_enable', )
    list_filter = ('name','leverage', 'min_deposit', 'is_enable', )
    search_fields = ('name','leverage', 'min_deposit', 'is_enable', )