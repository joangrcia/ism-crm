from django.contrib import admin
from .models import TradingAccount

# Register your models here.
@admin.register(TradingAccount)
class TradingAccountAdmin(admin.ModelAdmin):
    list_display = ('user','account_number', 'client_group',)
    list_filter = ('account_number', 'client_group')
    search_fields = ('user','account_number', 'client_group')
