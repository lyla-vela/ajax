from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core import serializers
# Create your views here.
def index(request):
    return render(request,"user_login/index.html")
def all_json(request):
    users=User.objects.all()
    users_json =serializers.serialize("json",users)
    return HttpResponse(users_json, content_type='application/json')
def all_html(request):
    users=User.objects.all()
    # context={'users:': users}
    return render(request,"user_login/all.html",{'users':users})
def find(request):
    return render(request, 'user_login/all.html',
    {'users': User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])})
def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return render(request, 'user_login/all.html',{'users': User.objects.order_by("-id")})