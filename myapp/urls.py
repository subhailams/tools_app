from django.conf.urls import  url
from myapp.views import base

urlpatterns = [
    url(r'', base, name = 'base'),
]
