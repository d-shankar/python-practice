from django.shortcuts import render
from django.http import HttpResponse
from ..model.practice import AccessRecord
from ..model.user import User

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    userList=User.objects.order_by('email')
    date_dict = {'access_record':webpages_list}

    return render(request,"index/index.html",date_dict)