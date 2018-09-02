#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.post_list, name='post_list')
]