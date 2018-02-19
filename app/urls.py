# -*- coding: utf-8 -*-
from django.urls import path
from app import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('list', views.List.as_view(), name='list'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>/', views.Update.as_view(), name='update'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]
