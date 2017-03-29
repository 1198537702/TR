from datetime import datetime

from ..models import User, Order, Driver
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import JsonResponse
from ..models import Order
from django.forms.models import modelform_factory

class userServiec:
    @staticmethod
    def login(request):
        phone = request.POST.get('tell', '')
        try:
            user = User.objects.get(tell=phone)
        except ObjectDoesNotExist:
            msg = '用户不存在'
            response = JsonResponse({'msg': msg}, safe=False)
        else:
            if user.password != request.POST.get('pass'):
                msg = '密码错误'
                response = JsonResponse({'msg': msg}, safe=False)

            else:
                user.password = ''
                msg = model_to_dict(user)
                response = JsonResponse({'msg': 'success', 'user': msg}, safe=False)

        return response

    @staticmethod
    def getOrderList(request):
        userId = request.GET.get('userId', '')
        status = request.GET.get('list', '')
        if status == 'finish':
            orderList = Order.objects.filter(userId=userId, finishTime__isnull=False).values()
        elif status == 'notfinish':
            orderList = Order.objects.filter(userId=userId, finishTime__isnull=True).values()
        msg = 'success'
        if len(orderList) == 0:
            msg = '还没有下过单呢~'
            response = JsonResponse({'msg': msg}, safe=False)
            return response

        else:
            response = JsonResponse({'msg': msg, 'orderList': list(orderList)}, safe=False)
            return response

    @staticmethod
    def getDriverInfo(request):
        driverId = request.GET.get('driverId', '')
        driver = Driver.objects.values('name', 'licensePlateNumber', 'headPortrait').get(tell=driverId)
        response = JsonResponse({'driver': driver}, safe=False)
        return response

    @staticmethod
    def newOrder(request):
        form = modelform_factory(Order, fields='__all__')
        o = form(request.POST)
        print(o.is_valid())
        print(o.errors)
        model = o.save()
        return JsonResponse({'msg': 'success'})

    @staticmethod
    def orderEvaluation(request):
        form = modelform_factory(Order, fields=('evaluation', 'mark', 'id'))

        o = form(request.POST)
        model = o.save(commit=False)
        model.id = request.POST.get('id')
        model.save(update_fields=['evaluation', 'mark'])
        return JsonResponse({'msg': 'success'})







