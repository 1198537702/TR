from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^orderTest', views.orderTest, name='orderTest'),

    url(r'^login', views.login, name='login'),
    url(r'^newOrder', views.newOrder, name='newOrder'),
    url(r'^userOrderList', views.userOrderList, name='userOrderList'),
    url(r'^driverInfo', views.driverInfo, name='driverInfo'),
    url(r'^orderEvaluation', views.orderEvaluation, name='orderEvaluation'),
    url(r'^confirmedService', views.confirmedService, name='confirmedService'),


    url(r'^driverOrderList', views.driverOrderList, name='driverOrderList'),
    url(r'^orderReceve', views.orderReceve, name='orderEvaluation'),
    url(r'^orderService', views.orderService, name='orderService'),
    url(r'^orderFinishedList', views.driverOrderFinishedList, name='orderFinishedList'),
    url(r'^uploadDriverImg', views.uploadDriverImg, name='uploadDriverImg'),
    url(r'^driverLogin', views.driverLogin, name='uploadDriverImg'),
]
