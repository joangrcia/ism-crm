from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.http import HttpResponse
from .models import ProductTrading
from django.views.decorators.http import require_http_methods
import json

from django_htmx.middleware import HtmxDetails

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

# Create your views here.
@require_http_methods(["GET"])
@login_required
def index(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, 'product_app/index.html')

def get(request: HtmxHttpRequest) -> HttpResponse:
    product = ProductTrading.objects.all().order_by('id')
    context = {
        'products': product,
    }
    return render(request, 'product_app/index-get.html', context)

@require_http_methods(["POST"])
def checker(request: HtmxHttpRequest) -> HttpResponse:
    if request.method == 'POST':
        post_data = request.POST
        product = get_object_or_404(ProductTrading, id=post_data['product_id'])
        
        # Menginisialisasi pesan
        showMessage = showMessage = f"{product.name} product has been saved."

        if 'group' in post_data:
            group = post_data['group']
            if group != product.name:
                product.name = group
                showMessage = f"{product.name} product name change has been successfully saved."

        if 'leverage' in post_data:
            leverage = post_data['leverage']
            if leverage != product.leverage:
                product.leverage = leverage
                
        if 'min_deposit' in post_data:
            min_deposit = post_data['min_deposit']
            if min_deposit != product.min_deposit:
                product.min_deposit = min_deposit

        if 'enables' in post_data:
            enables = post_data['enables'].lower() == 'true'
            if enables != product.is_enable:
                product.is_enable = enables
                showMessage = f"{product.name} product enable has been {'enabled' if enables else 'disabled'}."

        product.save()

        return HttpResponse(status=204,
                            headers={'HX-Trigger': json.dumps({
                                'productChange': None,
                                'showMessage': showMessage
                            })}
        )
@require_http_methods(["POST"])
def add(request: HtmxHttpRequest) -> HttpResponse:
    product = ProductTrading.objects.all().order_by('id')
    post_data = []
    if request.method == 'POST':
        post_data = request.POST
        nama = post_data['group']
        ProductTrading.objects.create(
            name=nama,
            leverage=int(post_data['leverage']),
            min_deposit=int(post_data['min-deposit']),
        )
        
    context = {
        'products': product
    }

    return HttpResponse(status=204,
                            headers={'HX-Trigger': json.dumps({
                                    'productChange':None,
                                    'showMessage':f'Product {nama} has been added'
                                }
        )})
@require_http_methods(["POST"])
def delete(request: HtmxHttpRequest) -> HttpResponse:

    if request.method == 'POST':
        product = get_object_or_404(ProductTrading, id=request.POST['product_id'])
        product.delete()

    return HttpResponse(status=204,
                            headers={'HX-Trigger': json.dumps({
                                    'productChange':None,
                                    'showMessage':f'Product {product.name} delete successfully.'
                                }
        )})