# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from banana.models import Topic,Webpage,AccessRecord

from django.shortcuts import render

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'banana/index.html',context=date_dict)
