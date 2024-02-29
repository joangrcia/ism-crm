from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import PersonalDetail
from apps.partner_app.models import IbAccount

def get_breadcrumb(path):
    parts = path.strip('/').split('/')
    breadcrumbs = [{'title': part.capitalize(), 'url': '/'.join(parts[:i+1])} for i, part in enumerate(parts)]
    return breadcrumbs

# Create your views here.
@login_required
def index(request):
    users = User.objects.all()
    ib_list = IbAccount.objects.all()

    context = {
        'page_obj': users,
        'ib_list' : ib_list,
    }
    return render(request, 'user_app/index.html', context)

@login_required
def verification(request):
    verification = PersonalDetail.objects.all()
    ib_list = IbAccount.objects.all()
    context = {
        'verification' : verification,
        'ib_list':ib_list,
    }
    return render(request, 'user_app/verification.html', context)