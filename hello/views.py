from django.shortcuts import render
from .models import TestTable
from .serializers import TestTableSerializer
from rest_framework import viewsets


# Create your views here.

def hello(request):
    infoList = TestTable.objects.all()
    context = {'InfoList': infoList}
    return render(request, 'hello/testpage.html', context)

class TestTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TestTable.objects.all()
    serializer_class = TestTableSerializer
