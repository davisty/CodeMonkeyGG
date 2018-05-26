# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'banana/homepage.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request, 'basicapp/form_page.html',{'form':form})
