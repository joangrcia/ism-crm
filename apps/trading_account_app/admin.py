from django.contrib import admin
from .models import TradingAccount, ProductTrading

# Register your models here.
@admin.register(TradingAccount)
class TradingAccountAdmin(admin.ModelAdmin):
    list_display = ('user','account_number', 'dm_group', 'account_deposit', 'created_at', 'last_updated',)
    list_filter = ('account_number', 'dm_group')
    search_fields = ('user','account_number', 'dm_group')