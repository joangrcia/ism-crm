from django.contrib import admin
from .models import TradingAccount

# Register your models here.
@admin.register(TradingAccount)
class TradingAccountAdmin(admin.ModelAdmin):
    list_display = ('user','account_number', 'client_group', 'account_deposit', 'created_at', 'last_updated',)
    list_filter = ('account_number', 'client_group')
    search_fields = ('user','account_number', 'client_group')
