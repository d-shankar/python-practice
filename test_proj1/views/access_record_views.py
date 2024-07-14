from django.shortcuts import render
from django.http import HttpResponse
from ..models.practice import AccessRecord

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpages_list}
    return render(request,"..templates/index.html")