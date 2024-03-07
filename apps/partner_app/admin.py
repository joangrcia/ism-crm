from django.contrib import admin
from .models import IbAccount, IbList, MibAccount

class IbListInline(admin.TabularInline):
    model = IbList
    extra = 1

class ib_accountAdmin(admin.ModelAdmin):
    inlines = [IbListInline]
    list_display = ('user', 'name', 'account_number', 'is_ib', 'is_sub_ib')
    exclude = ('is_ib', 'is_sub_ib',)

admin.site.register(IbAccount, ib_accountAdmin)

@admin.register(MibAccount)
class MibAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_confirm',)
    list_filter = ('is_confirm',)
    search_fields = ('user','user', 'is_confirm',)
