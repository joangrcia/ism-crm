from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Deposit, Withdraw, IntTrans, DepositHistory, WithdrawHistory, IntTransHistory
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from fast_pagination.helpers import FastPaginator
import json

from django_htmx.middleware import HtmxDetails

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

# Create your views here.
@login_required
def index(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, 'transaction_app/index.html')

@login_required
@require_http_methods(["GET"])
def deposit_get(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = Deposit.objects.select_related('user').filter(is_confirm=False).order_by('id')

            if search_query:
                mib_accounts = mib_accounts.filter(
                    Q(user__username__icontains=search_query) |
                    Q(user__email__icontains=search_query) |
                    Q(user__first_name__icontains=search_query) |
                    Q(user__last_name__icontains=search_query) |
                    Q(created_at__icontains=search_query)
                )

            per_page = 5 if request.GET.get('record') == None else request.GET.get('record')
            paginator = Paginator(mib_accounts, per_page)
            page_number = request.GET.get('page')
            
            try:
                mib_page = paginator.page(page_number)
            except PageNotAnInteger:
                mib_page = paginator.page(1)
            except EmptyPage:
                mib_page = paginator.page(paginator.num_pages)

        context = {
            'xreq': xreq,
            'mib': mib_page,
            'page_req': page_req,
        }

    return render(request, 'transaction_app/deposit-get.html', context)

@login_required
@require_http_methods(["GET"])
def deposit_history_get(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = DepositHistory.objects.select_related('user').all().order_by('id')

            if search_query:
                mib_accounts = mib_accounts.filter(
                    Q(user__username__icontains=search_query) |
                    Q(user__email__icontains=search_query) |
                    Q(user__first_name__icontains=search_query) |
                    Q(user__last_name__icontains=search_query) |
                    Q(created_at__icontains=search_query)
                )

            per_page = 5 if request.GET.get('record') == None else request.GET.get('record')
            paginator = Paginator(mib_accounts, per_page)
            page_number = request.GET.get('page')
            
            try:
                mib_page = paginator.page(page_number)
            except PageNotAnInteger:
                mib_page = paginator.page(1)
            except EmptyPage:
                mib_page = paginator.page(paginator.num_pages)

        context = {
            'xreq': xreq,
            'mib': mib_page,
            'page_req': page_req,
        }

    return render(request, 'transaction_app/deposit-history-get.html', context)

@require_http_methods(["POST"])
def deposit_update(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")

        if page_req == "ib":
            
            mib_account = get_object_or_404(Deposit, id=group_id)
            mib_account.is_confirm = not mib_account.is_confirm
            mib_account.save()

            DepositHistory.objects.create(
                user=mib_account.user,
                amount=mib_account.amount,
                account=mib_account.account,
                bank_method=mib_account.bank_method,
                status='Accepted',
                created_at=mib_account.created_at,
            )

    cache.delete('index_page_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@require_http_methods(["POST"])
def deposit_delete(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")

        if page_req == "ib":
            
            mib_account = get_object_or_404(Deposit, id=group_id)
            mib_account.delete()

            DepositHistory.objects.create(
                user=mib_account.user,
                amount=mib_account.amount,
                account=mib_account.account,
                bank_method=mib_account.bank_method,
                status='Rejected',
                created_at=mib_account.created_at,
            )

    cache.delete('index_page_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@login_required
def withdrawal(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, 'transaction_app/withdrawal.html')

@login_required
@require_http_methods(["GET"])
def withdrawal_get(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = Withdraw.objects.select_related('user').filter(is_confirm=False).order_by('id')

            if search_query:
                mib_accounts = mib_accounts.filter(
                    Q(user__username__icontains=search_query) |
                    Q(user__email__icontains=search_query) |
                    Q(user__first_name__icontains=search_query) |
                    Q(user__last_name__icontains=search_query) |
                    Q(created_at__icontains=search_query)
                )

            per_page = 5 if request.GET.get('record') == None else request.GET.get('record')
            paginator = Paginator(mib_accounts, per_page)
            page_number = request.GET.get('page')
            
            try:
                mib_page = paginator.page(page_number)
            except PageNotAnInteger:
                mib_page = paginator.page(1)
            except EmptyPage:
                mib_page = paginator.page(paginator.num_pages)

        context = {
            'xreq': xreq,
            'mib': mib_page,
            'page_req': page_req,
        }

    return render(request, 'transaction_app/withdrawal-get.html', context)

@login_required
@require_http_methods(["GET"])
def withdrawal_history_get(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = WithdrawHistory.objects.select_related('user').all().order_by('id')

            if search_query:
                mib_accounts = mib_accounts.filter(
                    Q(user__username__icontains=search_query) |
                    Q(user__email__icontains=search_query) |
                    Q(user__first_name__icontains=search_query) |
                    Q(user__last_name__icontains=search_query) |
                    Q(created_at__icontains=search_query)
                )

            per_page = 5 if request.GET.get('record') == None else request.GET.get('record')
            paginator = Paginator(mib_accounts, per_page)
            page_number = request.GET.get('page')
            
            try:
                mib_page = paginator.page(page_number)
            except PageNotAnInteger:
                mib_page = paginator.page(1)
            except EmptyPage:
                mib_page = paginator.page(paginator.num_pages)

        context = {
            'xreq': xreq,
            'mib': mib_page,
            'page_req': page_req,
        }

    return render(request, 'transaction_app/deposit-history-get.html', context)

@require_http_methods(["POST"])
def withdrawal_update(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")

        if page_req == "ib":
            
            mib_account = get_object_or_404(Withdraw, id=group_id)
            mib_account.is_confirm = not mib_account.is_confirm
            mib_account.save()

            WithdrawHistory.objects.create(
                user=mib_account.user,
                amount=mib_account.amount,
                account=mib_account.account,
                bank_method=mib_account.bank_method,
                status='Accepted',
                created_at=mib_account.created_at,
            )

    cache.delete('index_page_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@require_http_methods(["POST"])
def withdrawal_delete(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")

        if page_req == "ib":
            
            mib_account = get_object_or_404(Withdraw, id=group_id)
            mib_account.delete()

            WithdrawHistory.objects.create(
                user=mib_account.user,
                amount=mib_account.amount,
                account=mib_account.account,
                bank_method=mib_account.bank_method,
                status='Rejected',
                created_at=mib_account.created_at,
            )

    cache.delete('index_page_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@login_required
def internal_trans(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, 'transaction_app/internal_trans.html')

@login_required
@require_http_methods(["GET"])
def internal_trans_get(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = IntTrans.objects.select_related('user').filter(is_confirm=False).order_by('id')

            if search_query:
                mib_accounts = mib_accounts.filter(
                    Q(user__username__icontains=search_query) |
                    Q(user__email__icontains=search_query) |
                    Q(user__first_name__icontains=search_query) |
                    Q(user__last_name__icontains=search_query) |
                    Q(created_at__icontains=search_query)
                )

            per_page = 5 if request.GET.get('record') == None else request.GET.get('record')
            paginator = Paginator(mib_accounts, per_page)
            page_number = request.GET.get('page')
            
            try:
                mib_page = paginator.page(page_number)
            except PageNotAnInteger:
                mib_page = paginator.page(1)
            except EmptyPage:
                mib_page = paginator.page(paginator.num_pages)

        context = {
            'xreq': xreq,
            'mib': mib_page,
            'page_req': page_req,
        }

    return render(request, 'transaction_app/internal_trans-get.html', context)

@login_required
@require_http_methods(["GET"])
def internal_trans_history_get(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = IntTransHistory.objects.select_related('user').all().order_by('id')

            if search_query:
                mib_accounts = mib_accounts.filter(
                    Q(user__username__icontains=search_query) |
                    Q(user__email__icontains=search_query) |
                    Q(user__first_name__icontains=search_query) |
                    Q(user__last_name__icontains=search_query) |
                    Q(created_at__icontains=search_query)
                )

            per_page = 5 if request.GET.get('record') == None else request.GET.get('record')
            paginator = Paginator(mib_accounts, per_page)
            page_number = request.GET.get('page')
            
            try:
                mib_page = paginator.page(page_number)
            except PageNotAnInteger:
                mib_page = paginator.page(1)
            except EmptyPage:
                mib_page = paginator.page(paginator.num_pages)

        context = {
            'xreq': xreq,
            'mib': mib_page,
            'page_req': page_req,
        }

    return render(request, 'transaction_app/internal_trans-history-get.html', context)

@require_http_methods(["POST"])
def internal_trans_update(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")

        if page_req == "ib":
            
            mib_account = get_object_or_404(IntTrans, id=group_id)
            mib_account.is_confirm = not mib_account.is_confirm
            mib_account.save()

            IntTransHistory.objects.create(
                user=mib_account.user,
                amount=mib_account.amount,
                from_account=mib_account.from_account,
                to_account=mib_account.to_account,
                status='Accepted',
                created_at=mib_account.created_at,
            )

    cache.delete('index_page_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@require_http_methods(["POST"])
def internal_trans_delete(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")

        if page_req == "ib":
            
            mib_account = get_object_or_404(IntTrans, id=group_id)
            mib_account.delete()

            IntTransHistory.objects.create(
                user=mib_account.user,
                amount=mib_account.amount,
                from_account=mib_account.from_account,
                to_account=mib_account.to_account,
                status='Rejected',
                created_at=mib_account.created_at,
            )

    cache.delete('index_page_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})