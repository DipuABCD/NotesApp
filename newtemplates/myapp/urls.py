from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('category/',views.category),
   path('work/',views.work),
]