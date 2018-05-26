# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from user_app.models import User
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'banana/homepage.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'user_app/users.html',context=user_dict)
