from django.contrib import admin
from django.urls import path,include
from  . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('category/<str:name>/',views.category,name='category'),
    path('search/', views.search , name = 'search'),

]