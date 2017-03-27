from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^orderTest', views.orderTest, name='orderTest'),
    url(r'^login', views.login, name='login'),
    url(r'^newOrder', views.newOrder, name='newOrder'),
    url(r'^userOrderList', views.userOrderList, name='userOrderList'),
    url(r'^driverInfo', views.driverInfo, name='driverInfo'),
    url(r'^orderEvaluation', views.orderEvaluation, name='orderEvaluation'),
]
