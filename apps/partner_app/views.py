from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'partner_app/index.html')

@login_required
def wallet(request):
    return render(request, 'partner_app/wallet.html')

@login_required
def verification(request):
    return render(request, 'partner_app/verification.html')

@login_required
def request(request):
    return render(request, 'partner_app/request.html')