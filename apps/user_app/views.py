from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import PersonalDetail,BankDetail, Wallet
from apps.trading_account_app.models import TradingAccount
from apps.partner_app.models import IbAccount, IbList
import json
from django.http import JsonResponse
from django.db.models import Prefetch
from django.core.serializers.json import DjangoJSONEncoder

def get_breadcrumb(path):
    parts = path.strip('/').split('/')
    breadcrumbs = [{'title': part.capitalize(), 'url': '/'.join(parts[:i+1])} for i, part in enumerate(parts)]
    return breadcrumbs


@login_required
def index(request):
    return render(request, 'user_app/index.html')

def get_users(request):
    start = int(request.POST.get('start', 0))
    length = int(request.POST.get('length', 100))
    filter_by = request.POST.get('filter_by', "")
    filter_value = request.POST.get('filter_value', "")

    total_records = User.objects.count()

    if length == 0:
        length = total_records

    users = User.objects.prefetch_related(
        Prefetch('personaldetail', queryset=PersonalDetail.objects.all()),
        Prefetch('personaldetail__bankdetail', queryset=BankDetail.objects.all()),
        Prefetch('personaldetail__wallet', queryset=Wallet.objects.all()),
        Prefetch('tradingaccount_set', queryset=TradingAccount.objects.all()),
        Prefetch('ib_lists', queryset=IbList.objects.all())  
    ).order_by('id')

    if filter_by and filter_value:
        
        users = users.filter(**{filter_by: filter_value})

    filtered_users = users[start:start + length]  
    filtered_records = len(filtered_users)  

    if length != total_records:
        filtered_records = min(filtered_records, length)

    users = users[start:start + length]

    data = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'last_login': user.last_login,
            'is_superuser': user.is_superuser,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active,
            'date_joined': user.date_joined,
            'trading_accounts': [],
            'ib_lists': []  
        }

        
        for account in user.tradingaccount_set.all():
            trading_account_data = {
                'account_number': account.account_number,
                'account_deposit': account.account_deposit,
                'dm_group': account.dm_group.id,  
                'created_at': account.created_at,
                'last_updated': account.last_updated
            }
            user_data['trading_accounts'].append(trading_account_data)

        
        try:
            ib_list = user.ib_lists
            if ib_list:  
                ib_list_data = {
                    'ib': ib_list.ib.name
                }
                user_data['ib_lists'] = [ib_list_data]
            else:
                user_data['ib_lists'] = None
        except IbList.DoesNotExist:
            user_data['ib_lists'] = None

        try:
            personal_detail = user.personaldetail
            user_data['personalDetail'] = {
                'phone': str(personal_detail.phone),
                'id_number': personal_detail.id_number,
                'marital_status': personal_detail.marital_status,
                'country': personal_detail.country,
                'state': personal_detail.state,
                'city': personal_detail.city,
                'postal': personal_detail.postal,
                'address': personal_detail.address,
                'last_updated': personal_detail.last_updated,
            }

            bank_detail = personal_detail.bankdetail
            user_data['bankDetail'] = {
                'account_name': bank_detail.account_name,
                'bank_account': bank_detail.bank_account,
                'bank_address': bank_detail.bank_address,
                'swift_code': bank_detail.swift_code,
                'bank_name': bank_detail.bank_name,
            }
        except PersonalDetail.DoesNotExist:
            user_data['personalDetail'] = None
            user_data['bankDetail'] = None

        data.append(user_data)


    if not filter_by or not filter_value:
       filtered_records = total_records

    response = {
        'recordsTotal': total_records,
        'recordsFiltered': filtered_records,
        'data': data
    }

    return JsonResponse(response, safe=False, encoder=DjangoJSONEncoder)


@login_required
def verification(request):
    return render(request, 'user_app/verification.html')

def get_verification(request):
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 0))
    filter_by = request.GET.get('filter_by', '')
    filter_value = request.GET.get('filter_value', '')

    total_records = PersonalDetail.objects.count()

    if length == 0:
        length = total_records

    verification = PersonalDetail.objects.select_related('user').all()

    if filter_by and filter_value:
        
        verification = verification.filter(**{filter_by: filter_value})

    filtered_verify = verification[start:start + length]  
    filtered_records = len(filtered_verify)  

    if length != total_records:
        filtered_records = min(filtered_records, length)

    verification = verification[start:start + length]

    data = []
    for verify in verification:
        verify_data = {
            'last_updated': verify.last_updated,
            'first_name': verify.first_name,
            'last_name': verify.last_name,
            'username': verify.user.username,
            'email': verify.email,
            'phone': str(verify.phone),
            'city': verify.city
        } 

        data.append(verify_data)

    if not filter_by or not filter_value:
       filtered_records = total_records

    response = {
        'recordsTotal': total_records,
        'recordsFiltered': filtered_records,
        'data': data
    }

    return JsonResponse(response, safe=False, encoder=DjangoJSONEncoder)