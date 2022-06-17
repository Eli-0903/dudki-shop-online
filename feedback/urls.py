from django.urls import path
from . import views
from django.contrib import admin
from .views import index, create

urlpatterns = [
    path("/", admin.site.urls),
    
    path('', views.index),
    path("creat/", create, name = "creat")
]
