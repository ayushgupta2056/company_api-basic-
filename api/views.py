from rest_framework import viewsets
from api.models import company,employee
from api.serilizers import CompanySerializer,employeeserializer


# Create your views here.
class companyViewset(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=CompanySerializer

class employeeviewset(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employeeserializer