from django.contrib import admin
from .models import IbAccount, IbList

# Register your models here.
@admin.register(IbAccount)
class ib_accountAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'account_number', 'is_confirmed')
    # list_filter = ('account_number', 'client_group')
    # search_fields = ('user','account_number', 'client_group')

@admin.register(IbList)
class IbListAdmin(admin.ModelAdmin):
    list_display = ('ib','client_account')
    # list_filter = ('account_number', 'client_group')
    # search_fields = ('user','account_number', 'client_group')
