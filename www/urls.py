from django.conf.urls import (
    url,
    include,
)
from django.contrib import admin
from app1 import views

urlpatterns = [
    url(r'^', include('app1.urls')),
]