from rest_framework import serializers

from api.models import company, employee
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=company
        fields="__all__"

class employeeserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=employee
        fields="__all__"
