from django.http import JsonResponse
from django.forms.models import modelform_factory
from django.views.decorators.csrf import csrf_exempt

from .service.user import *
from .tool.myResponse import MyResponse


# Create your views here.

def orderTest(request):
    if request.method == 'GET':
        order = Order.objects.values('id', 'transportTime', 'start',
                                     'end', 'orderStatus', 'pay').all()

        response = JsonResponse(list(order), safe=False)
        return response


def login(request):
    user = userServiec()
    return user.login(request)


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