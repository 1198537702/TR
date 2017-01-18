from django.shortcuts import render
from .models import TestTable


# Create your views here.

def hello(request):
    infoList = TestTable.objects.all()
    print(type(request))
    context = {'testInfo': infoList}
    return render(request, 'hello/testpage.html', context)
