from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import PersonalDetail,BankDetail, Wallet
from apps.partner_app.models import IbAccount
import json
from django.http import JsonResponse
from django.db.models import Prefetch
from django.core.serializers.json import DjangoJSONEncoder

def get_breadcrumb(path):
    parts = path.strip('/').split('/')
    breadcrumbs = [{'title': part.capitalize(), 'url': '/'.join(parts[:i+1])} for i, part in enumerate(parts)]
    return breadcrumbs

# Create your views here.
@login_required
def index(request):
    """
    users = User.objects.all()
    ib_list = IbAccount.objects.all()

    context = {
        'page_obj': users,
        'ib_list' : ib_list,
    }
    """
    return render(request, 'user_app/index.html')

def get_users(request):
    start = int(request.POST.get('start'))
    length = int(request.POST.get('length'))
    filter_by = request.POST.get('filter_by')
    filter_value = request.POST.get('filter_value')

    total_records = User.objects.count()

    if length == 0:
        length = total_records

    users = User.objects.prefetch_related(
        Prefetch('personaldetail', queryset=PersonalDetail.objects.all()),
        Prefetch('personaldetail__bankdetail',
                 queryset=BankDetail.objects.all()),
        Prefetch('personaldetail__wallet', queryset=Wallet.objects.all())
    ).order_by('id')

    if filter_by and filter_value:
        # Filter users based on filter_by field dynamically
        users = users.filter(**{filter_by: filter_value})

    filtered_users = users[start:start + length]  # Apply pagination using slicing
    filtered_records = len(filtered_users)  # Count the number of filtered records after pagination

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
            'date_joined': user.date_joined
        }

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
            pass

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
    """
    verification = PersonalDetail.objects.all()
    ib_list = IbAccount.objects.all()
    context = {
        'verification' : verification,
        'ib_list':ib_list,
    }
    """
    return render(request, 'user_app/verification.html')

def get_verification(request):
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 0))
    filter_by = request.GET.get('filter_by', '')
    filter_value = request.GET.get('filter_value', '')

    total_records = PersonalDetail.objects.count()

    if length == 0:
        length = total_records

    verification = PersonalDetail.objects.all()

    if filter_by and filter_value:
        # Filter users based on filter_by field dynamically
        verification = verification.filter(**{filter_by: filter_value})

    filtered_verify = verification[start:start + length]  # Apply pagination using slicing
    filtered_records = len(filtered_verify)  # Count the number of filtered records after pagination

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