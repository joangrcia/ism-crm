from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
    return render(request, "dashboard_app/index.html")

@login_required
def indexLogout(request):
    logout(request)
    return redirect('login')