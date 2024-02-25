from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'transaction_app/index.html')

@login_required
def withdrawal(request):
    return render(request, 'transaction_app/withdrawal.html')

@login_required
def internal_trans(request):
    return render(request, 'transaction_app/internal_trans.html')