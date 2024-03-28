from django.shortcuts import render, get_object_or_404
from .models import MibAccount, IbAccount, MibList, IbList, History
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseBadRequest
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_http_methods
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from fast_pagination.helpers import FastPaginator

from django_htmx.middleware import HtmxDetails

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

# Create your views here.
@login_required
# @cache_page(60*15, key_prefix='index_page_cache_key')
def index(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, 'partner_app/index.html')

# @cache_page(60*15)
@login_required
@require_http_methods(["GET"])
def partner_get(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = IbAccount.objects.select_related('user').filter(Q(is_confirm=True)).order_by("id")

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

        elif page_req == "mib":
            search_query = request.GET.get('simple-search', '')
            xreq = page_req
            mib_accounts = MibAccount.objects.select_related('user').filter(Q(is_confirm=True)).order_by('id')

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

    return render(request, 'partner_app/partner-get.html', context)

@require_http_methods(["POST"])
def partner_update(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")
        
        if page_req == "ib":
            
            mib_account = get_object_or_404(IbAccount, id=group_id)
            mib_account.active = not mib_account.active
            mib_account.save()

        elif page_req == "mib":
            
            mib_account = get_object_or_404(MibAccount, id=group_id)
            mib_account.active = not mib_account.active
            mib_account.save()

    cache.delete('index_page_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@login_required
def wallet(request):
    return render(request, 'partner_app/wallet.html')

@login_required
# @cache_page(60*15, key_prefix='verify_cache_key')
def verification(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, 'partner_app/verification.html')

@login_required
@require_http_methods(["GET"])
def history_get(request: HtmxHttpRequest) -> HttpResponse:
    search_query = request.GET.get('simple-search', '')
    mib_accounts = History.objects.select_related('user').all().order_by('id')

    if search_query:

        mib_accounts = mib_accounts.filter(
            Q(user__username__icontains=search_query) |
            Q(user__email__icontains=search_query) |
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(status__icontains=search_query) |
            Q(request__icontains=search_query) |
            Q(created_at__icontains=search_query)
        )

    per_page = 10 if request.GET.get('record') == None else request.GET.get('record')
    paginator = Paginator(mib_accounts, per_page)
    page_number = request.GET.get('page')

    try:
        mib_page = paginator.page(page_number)
    except PageNotAnInteger:
        mib_page = paginator.page(1)
    except EmptyPage:
        mib_page = paginator.page(paginator.num_pages)

    context = {
        'mib': mib_page,
    }
    return render(request, 'partner_app/history-get.html', context)

@login_required
@require_http_methods(["GET"])
def verify_get(request: HtmxHttpRequest) -> HttpResponse:
    if request.method == "GET":
        page_req = request.GET.get('req')
        if page_req == "ib":

            xreq = page_req
            mib_accounts = IbAccount.objects.select_related('user').filter(Q(is_confirm=False)).order_by('id')
            per_page = 3
            paginator = Paginator(mib_accounts, per_page)
            page_number = request.GET.get('page')
            try:
                mib_page = paginator.page(page_number)
            except PageNotAnInteger:
                mib_page = paginator.page(1)
            except EmptyPage:
                mib_page = paginator.page(paginator.num_pages)

        elif page_req == "mib":
            
            xreq = page_req
            mib_accounts = MibAccount.objects.select_related('user').filter(Q(is_confirm=False))
            per_page = 3
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
            'page_req': page_req,  # Mengirimkan parameter 'req' ke template
        }

    return render(request, 'partner_app/verification-get.html', context)

@require_http_methods(["POST"])
def verify_update(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")
        
        if page_req == "ib":
            
            mib_account = get_object_or_404(IbAccount, id=group_id)
            mib_account.is_confirm = True
            mib_account.save()

            History.objects.create(
                user=mib_account.user,
                status="Accepted",
                request="IB"
            )

        elif page_req == "mib":
            
            mib_account = get_object_or_404(MibAccount, id=group_id)
            mib_account.is_confirm = True
            mib_account.save()

            History.objects.create(
                user=mib_account.user,
                status="Accepted",
                request="MIB"
            )

    cache.delete('verify_cache_key')
    showMessage = "Product has been saved."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@require_http_methods(["POST"])
def verify_delete(request: HtmxHttpRequest) -> JsonResponse:
    if request.method == 'POST':
        group_id = request.POST.get('group')
        page_req = request.POST.get('req')
        if not group_id:
            return HttpResponseBadRequest("Group ID is required.")
        
        if page_req == "ib":

            mib_account = get_object_or_404(IbAccount, id=group_id)
            mib_account.delete()
            History.objects.create(
                user=mib_account.user,
                status="Rejected",
                request="IB"
            )
        
        if page_req == "mib":

            mib_account = get_object_or_404(MibAccount, id=group_id)
            mib_account.delete()
            History.objects.create(
                user=mib_account.user,
                status="Rejected",
                request="MIB"
            )

    cache.delete('verify_cache_key')
    showMessage = "MibAccount has been deleted."
    response_data = {
        'productChange': None,
        'showMessage': showMessage
    }
    return JsonResponse(response_data, status=204, headers={'HX-Trigger': json.dumps(response_data)})

@login_required
def request(request):
    return render(request, 'partner_app/request.html')