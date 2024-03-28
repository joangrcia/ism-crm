from django.contrib import admin
from .models import IbAccount, IbList, MibAccount, MibList, History

def confirm_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.is_confirm = not obj.is_confirm
        obj.save()

confirm_selected.short_description = "Confirm selected items"

class IbListInline(admin.TabularInline):
    model = IbList
    extra = 1

class ib_accountAdmin(admin.ModelAdmin):
    inlines = [IbListInline]
    list_display = ('user', 'name', 'account_number', 'is_confirm', 'is_ib', 'is_sub_ib', 'active')
    exclude = ('is_ib', 'is_sub_ib',)
    actions = [confirm_selected]

admin.site.register(IbAccount, ib_accountAdmin)

class MibListInline(admin.TabularInline):
    model = MibList
    extra = 1

@admin.register(MibAccount)
class MibAccountAdmin(admin.ModelAdmin):
    inlines = [MibListInline]
    list_display = ('user', 'is_confirm', 'active')
    list_filter = ('is_confirm', 'active')
    search_fields = ('user','user', 'is_confirm', 'active')
    actions = [confirm_selected]

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'request', 'created_at')
    list_filter = ('status', 'request')
    search_fields = ('user', 'status', 'request')
