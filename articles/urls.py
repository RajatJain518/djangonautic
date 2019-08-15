from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    re_path(r'^$',views.article_list, name="list"),
    re_path(r'^create/$', views.article_create, name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    
]
