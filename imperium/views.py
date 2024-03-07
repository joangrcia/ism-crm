from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext as _
import json
from django.http import JsonResponse
from django.db.models import Prefetch
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from apps.user_app.models import PersonalDetail, BankDetail, Wallet
from django.views.decorators.http import require_GET, require_POST


def get_breadcrumb(path):
    parts = path.strip('/').split('/')
    breadcrumbs = [{'title': part.capitalize(), 'url': '/'.join(parts[:i+1])}
                   for i, part in enumerate(parts)]
    return breadcrumbs


def index(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        else:
            return render(request, 'index.html')

    if request.method == 'POST':

        print(request.POST)

        username_login = request.POST.get('username')
        password_login = request.POST.get('password')

        user = authenticate(request, username=username_login,
                            password=password_login)

        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            messages.info(request, "Username or password incorrect.")
            return redirect('two_factor:login')


def send_email(request):
    return render(request, 'send_email.html')

# Fungsi penanganan 404


def handler404(request, exception):
    return render(request, '404.html', status=404)

# Fungsi penanganan 505


def handler505(request, exception):
    return render(request, '505.html', status=505)



def all_users(request):
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 0))
    filter_by = request.GET.get('filter_by', '')
    filter_value = request.GET.get('filter_value', '')


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

    response = {
        'recordsTotal': total_records,
        'recordsFiltered': filtered_records,
        'data': data
    }

    return JsonResponse(response, safe=False, encoder=DjangoJSONEncoder)
