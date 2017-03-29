from ..models import User, Order, Driver
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import JsonResponse
from ..models import Order
from django.forms.models import modelform_factory

class driverServiec:
    @staticmethod
    def login(request):
        phone = request.POST.get('tell', '')
        try:
            driver = Driver.objects.get(tell=phone)
        except ObjectDoesNotExist:
            msg = '用户不存在'
            response = JsonResponse({'msg': msg}, safe=False)
        else:
            if driver.password != request.POST.get('pass'):
                msg = '密码错误'
                response = JsonResponse({'msg': msg}, safe=False)

            else:
                driver.password = ''
                msg = model_to_dict(driver)
                response = JsonResponse({'msg': 'success', 'driver': msg}, safe=False)

        return response

    @staticmethod
    def getOrderList(request):
        orderList = Order.objects.filter(orderStatus='派车中').values()
        response = JsonResponse({'orderList': list(orderList)}, safe=False)
        return response


    @staticmethod
    def getOrderFinished(request):
        orderList = Order.objects.filter(orderStatus='已完成', driverId=request.GET.get('driverId')).values()
        response = JsonResponse({'orderList': list(orderList)}, safe=False)
        return response


    @staticmethod
    def orderReceve(request):
        form = modelform_factory(Order, fields=('driverId', 'recevingTime'))
        o = form(request.POST)
        model = o.save(commit=False)
        model.id = request.POST.get('id')
        model.orderStatus = '运送中'
        model.save(update_fields=['driverId', 'recevingTime', 'orderStatus'])
        return JsonResponse({'msg': 'success'})

    @staticmethod
    def orderService(request):
        m = Order(serviceTime=request.POST.get('serviceTime'))
        m.id = request.POST.get('id')
        m.orderStatus = '已送达'
        m.save(update_fields=['serviceTime', 'orderStatus'])
        return JsonResponse({'msg': 'success'})









