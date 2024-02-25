from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'social_trading_app/index.html')

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