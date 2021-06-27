from dongi.models import user
from django import forms
from django.urls import path
from . import views
app_name='dongi'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/index', views.userV.index, name='user_index'),
    path('user/create', views.userV.create, name='user_create'),
    path('user/', views.userV.index, name='user_index'),
    path('user/delete/<int:id>',views.userV.delete, name='user_delete'),
    path('user/edit/<int:id>',views.userV.edit, name='user_edit')


]