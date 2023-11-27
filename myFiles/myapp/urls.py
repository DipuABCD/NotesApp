from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
   path('',views.index),
   path('Notes/',views.Notes,name='notes'),
   path('profile/',views.profile),
   path('about/',views.about),
   path('contact/',views.contact),
   path('userlogout/',views.userlogout),
]