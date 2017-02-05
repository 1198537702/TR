from django.shortcuts import render
from .models import TestTable


# Create your views here.

def hello(request):
    infoList = TestTable.objects.all()
    context = {'InfoList': infoList}
    return render(request, 'hello/testpage.html', context)
