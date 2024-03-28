from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.db.models import Prefetch
from django.core.serializers.json import DjangoJSONEncoder

from .models import TradingAccount

@login_required
def index(request):

    return render(request, 'trading_account_app/index.html')

@login_required
# @require_GET
def get_taccount(request):
    start = int(request.POST.get('start'))
    length = int(request.POST.get('length'))
    filter_by = request.POST.get('filter_by')
    filter_value = request.POST.get('filter_value')

    total_records = TradingAccount.objects.count()

    if length == 0:
        length = total_records

    users = TradingAccount.objects.select_related('user').order_by('id')

    if filter_by and filter_value:

        users = users.filter(**{filter_by: filter_value})

    filtered_users = users[start:start + length]
    filtered_records = len(filtered_users)

    if length != total_records:
        filtered_records = min(filtered_records, length)

    data = []
    for user in filtered_users:
        user_data = {
            'id': str(user.id),
            'user': str(user.user.email),
            'account_number': int(user.account_number),
            'dm_group': str(user.dm_group),
            'account_deposit': int(user.account_deposit),
            'created_at': str(user.created_at),
            'last_updated': str(user.last_updated),
        }
        data.append(user_data)

    if not filter_by or not filter_value:
        filtered_records = total_records

    response = {
        'recordsTotal': total_records,
        'recordsFiltered': filtered_records,
        'data': data
    }

    return JsonResponse(response, safe=False, encoder=DjangoJSONEncoder)
