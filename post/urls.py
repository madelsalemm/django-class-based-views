from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.Post_List.as_view() , name='postlist'),
    path('<int:pk>', views.Post_Detail.as_view() , name='postdetail'),
]
