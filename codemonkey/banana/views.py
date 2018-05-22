# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hellow I am from views.py!"}
    return render(request,'banana/index.html',context=my_dict)
