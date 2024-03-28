from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django_htmx.middleware import HtmxDetails

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

# Create your views here.
@login_required
def index(request: HtmxHttpRequest) -> HttpResponse:
    page_num = int(request.GET.get("page", "1"))
    users = User.objects.all()
    paginator = Paginator(users, per_page=10)
    page = paginator.get_page(page_num)

    if request.htmx:
        base_template = "_partial.html"
    else:
        base_template = "base.html"

    return render(request, 'social_trading_app/index.html',
                  {
                      'base_template':base_template,
                      'page': page
                    })

@login_required
def subscription(request):
    return render(request, 'social_trading_app/subscription.html')

@login_required
def fee(request):
    return render(request, 'social_trading_app/fee.html')

@login_required
def master_fee(request):
    return render(request, 'social_trading_app/master_fee.html')

@login_required
def configuration(request):
    return render(request, 'social_trading_app/configuration.html')