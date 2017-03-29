from django.http import JsonResponse
from django.forms.models import modelform_factory
from django.views.decorators.csrf import csrf_exempt

from app.service.driver import driverServiec
from .service.user import *
from .tool.myResponse import MyResponse


# Create your views here.

def orderTest(request):
    if request.method == 'GET':
        order = Order.objects.values('id', 'transportTime', 'start',
                                     'end', 'orderStatus', 'pay').all()

        response = JsonResponse(list(order), safe=False)
        return response

# -----------------用户端---------------------
@csrf_exempt
def login(request):
    return userServiec.login(request)


@csrf_exempt
def newOrder(request):
    return userServiec.newOrder(request)

def userOrderList(request):
    return userServiec.getOrderList(request)


def driverInfo(request):
    return userServiec.getDriverInfo(request)

@csrf_exempt
def orderEvaluation(request):
    return userServiec.orderEvaluation(request)


# -----------------司机端---------------------
def driverOrderList(request):
    return driverServiec.getOrderList(request)


def driverOrderFinishedList(request):
    return driverServiec.getOrderFinished(request)

@csrf_exempt
def orderReceve(request):
    return driverServiec.orderReceve(request)


@csrf_exempt
def driverLogin(request):
    return driverServiec.login(request)

@csrf_exempt
def orderService(request):
    return driverServiec.orderService(request)





