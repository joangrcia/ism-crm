from django.contrib import admin
from .models import PersonalDetail, BankDetail

class BankDetailInline(admin.TabularInline):
    model = BankDetail
    extra = 5

class PersonalDetailAdmin(admin.ModelAdmin):
    inlines = [BankDetailInline]
    list_display = ('email', 'first_name', 'last_name', 'phone', 'id_type', 'id_number', 'marital_status', 'country', 'state', 'city', 'postal', 'address')

admin.site.register(PersonalDetail, PersonalDetailAdmin)
