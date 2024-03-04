
from django.contrib import admin
from django.urls import path

from Vapp import  views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home),
    path('Gallery/', views.images),
    path('About/', views.about),
    path('Contact/', views.contact),
    path('collection/', views.collection),
]




