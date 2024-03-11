from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.http import HttpResponse
from .models import ProductTrading

from django_htmx.middleware import HtmxDetails

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

# Create your views here.
@login_required
def index(request: HtmxHttpRequest) -> HttpResponse:
    product = ProductTrading.objects.all().order_by('id')
    context = {
        'products': product,
    }
    return render(request, 'product_app/index.html', context)


def checker(request: HtmxHttpRequest) -> HttpResponse:
    if request.method == 'POST':
        post_data = request.POST
        product = ProductTrading.objects.get(id=request.POST['product_id'])
        enables = post_data.get('enables', '')
        if enables.lower() == 'false':
            enables = False
        else:
            enables = True
        product.is_enable = enables
        product.name = request.POST['group']
        product.leverage = request.POST['leverage']
        product.min_deposit = request.POST['min-deposit']
        product.save()
        
    context = {
        'product':product
    }

    print(request.POST)

    return render(request, 'product_app/index-checker.html', context)