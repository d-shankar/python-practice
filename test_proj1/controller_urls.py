from django.urls import path, re_path
from django.contrib import admin
from test_proj1 import controllers
from test_proj1.views import access_record_views
urlpatterns =[
    re_path('test2/', controllers.index_message2, name = 'index_message2' ),
    re_path('index/', controllers.render_index, name='render_index'),
    re_path('access_Record', access_record_views.index, name = 'access_record_view'),
]

