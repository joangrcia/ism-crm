from django.contrib import admin
from .models import PersonalDetail, BankDetail, Wallet

class BankDetailInline(admin.TabularInline):
    model = BankDetail
    extra = 5

class PersonalDetailAdmin(admin.ModelAdmin):
    inlines = [BankDetailInline]
    list_display = ('email', 'first_name', 'last_name', 'phone', 'id_type', 'id_number', 'marital_status', 'country', 'state', 'city', 'postal', 'address',)

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user','wallet')

admin.site.register(PersonalDetail, PersonalDetailAdmin)
