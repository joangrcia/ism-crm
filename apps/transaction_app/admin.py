from django.contrib import admin
from .models import Deposit, DepositHistory, Withdraw, WithdrawHistory, IntTrans, IntTransHistory

def confirm_selected(modeladmin, request, queryset):
    for obj in queryset:
        obj.is_confirm = not obj.is_confirm
        obj.save()

# Register your models here.
@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'account', 'bank_method', 'is_confirm', 'created_at')
    list_filter = ('amount', 'bank_method', 'is_confirm', 'created_at')
    search_fields = ('user__username',)
    actions = [confirm_selected]

@admin.register(DepositHistory)
class DepositHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'account', 'bank_method', 'status', 'created_at')
    list_filter = ('amount', 'bank_method', 'status', 'created_at')
    search_fields = ('user__username', )
    actions = [confirm_selected]
    
@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'account', 'bank_method', 'is_confirm', 'created_at')
    list_filter = ('amount', 'bank_method', 'is_confirm', 'created_at')
    search_fields = ('user__username', )
    actions = [confirm_selected]

@admin.register(WithdrawHistory)
class WithdrawHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'account', 'bank_method', 'status', 'created_at')
    list_filter = ('amount', 'bank_method', 'status', 'created_at')
    search_fields = ('user__username', )
    actions = [confirm_selected]

@admin.register(IntTrans)
class IntTransAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'to_account', 'from_account', 'is_confirm', 'created_at')
    list_filter = ('amount', 'is_confirm', 'created_at')
    search_fields = ('user__username', )
    actions = [confirm_selected]

@admin.register(IntTransHistory)
class IntTransHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'to_account', 'from_account', 'status', 'created_at')
    list_filter = ('amount', 'status', 'created_at')
    search_fields = ('user__username', )
    actions = [confirm_selected]
