from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the bnb index.")


def login(request):
    return render(request, 'bnb/login.html')


def register(request):
    return render(request, 'bnb/register.html')


def add_user(request):
    if request.POST['password'] != request.POST['confirm_password']:
        messages.error(request,
                       'Password and Confirm Password are inconsistent')
        return HttpResponseRedirect(reverse('bnb:register'))
    elif not isvalid_mailformat(request.POST['password']):
        messages.error(request,
                       'Email format is not valid')
        return HttpResponseRedirect(reverse('bnb:register'))
    else:
        account = request.POST['account']
        if User.objects.filter(account=account).exists():
            messages.error(request,
                           'The account has already existed')
            return HttpResponseRedirect(reverse('bnb:register'))
        else:
            password = request.POST['password']
            name = request.POST['name']
            mail = request.POST['mail']
            user = User(account=account,
                        password=password,
                        name=name,
                        mail=mail)
            user.save()
            return HttpResponseRedirect(reverse('bnb:login'))


def isvalid_mailformat(mail):
    if '@' not in mail or '.' not in mail:
        return False
    else:
        return True


def identification(request):
    account = request.POST['account']
    request.session['_old_post'] = request.POST
    if User.objects.filter(account=account).exists():
        user = User.objects.get(account=account)
        if user.isadmin:
            return HttpResponseRedirect(reverse('bnb:admin_page'))
        else:
            return HttpResponseRedirect(reverse('bnb:user_page'))
    else:
        messages.error(request,
                       'This user is not registered yet')
        return HttpResponseRedirect(reverse('bnb:login'))


def user_page(request):
    old_post = request.session.get('_old_post')
    account = old_post['account']
    user = User.objects.get(account=account)
    context = {'user': user}
    return render(request, 'bnb/user_page.html', context)


def admin_page(request):
    return render(request, 'bnb/admin_page.html')