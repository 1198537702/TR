from rest_framework import serializers
from hello.models import TestTable


class TestTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTable
        fields = ('id', 'image')
