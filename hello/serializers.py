from rest_framework import serializers
from hello.models import TestTable


class TestTableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestTable
        fields = ('testInfo', 'id')
