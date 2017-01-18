from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^testTable/$', views.hello, name='hello-testTable'),
]