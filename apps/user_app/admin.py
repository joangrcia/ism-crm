from django.contrib import admin
from .models import PersonalDetail, BankDetail

class BankDetailInline(admin.TabularInline):
    model = BankDetail
    extra = 5

class PersonalDetailAdmin(admin.ModelAdmin):
    inlines = [BankDetailInline]

admin.site.register(PersonalDetail, PersonalDetailAdmin)
