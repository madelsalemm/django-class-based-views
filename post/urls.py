from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list , name='post'),
    path('<int:id>', views.post_detail , name='post'),
]
