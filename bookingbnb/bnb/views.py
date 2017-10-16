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
