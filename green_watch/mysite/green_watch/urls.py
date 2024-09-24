from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('', views.about),
    path('', views.contact),
    path('', views.events),
    path('', views.login),
    path('', views.recycleCenter),
    path('', views.register),
    path('', views.report),
]