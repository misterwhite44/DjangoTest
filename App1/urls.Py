from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('result/<int:number>/', views.result, name="result"),  
]
