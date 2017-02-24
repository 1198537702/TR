from django.shortcuts import render
from .models import TestTable
from .serializers import TestTableSerializer
from rest_framework import viewsets
from .forms import UploadFileForm


# Create your views here.

def hello(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = TestTable()
            instance.id = 1
            instance.testInfo = request.FILES['title']
            instance.image = request.FILES['file']
            instance.save()
            return 'success'
    else:
        form = UploadFileForm()
        InfoList = TestTable.objects.all()
    return render(request, 'hello/testpage.html', {'form': form, 'InfoList': InfoList})


class TestTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TestTable.objects.all()
    serializer_class = TestTableSerializer
