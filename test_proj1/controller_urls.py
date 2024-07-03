from django.urls import path, re_path
from django.contrib import admin
from test_proj1 import controllers
urlpatterns =[
    re_path('/test2',controllers.index_message2,name = 'index_message2' )
]

