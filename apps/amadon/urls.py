from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^/process/(?P<id>\d)$', views.process),  
    url(r'^/checkout$', views.checkout),   
    url(r'^$', views.index),
]