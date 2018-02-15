from django.conf.urls import url
from django.conf import settings
from . import (
    views,
)

urlpatterns = [
    url(r'^$', views.home_view, name='home_view')
	]