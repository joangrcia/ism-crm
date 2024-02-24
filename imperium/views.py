from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def index(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect ('dashboard:index')
        else:
            return render(request, 'index.html')

    if request.method == 'POST':
        
        print(request.POST)
        
        username_login = request.POST.get('username')
        password_login = request.POST.get('password')

        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            messages.info(request, "Username or password incorrect.")
            return redirect('login')
        
# Fungsi penanganan 404
def handler404(request, exception):
    return render(request, '404.html', status=404)

# Fungsi penanganan 505
def handler505(request, exception):
    return render(request, '505.html', status=505)