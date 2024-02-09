from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import ComanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=ComanySerializer

    @action(detail=True,  methods=['get'])
    def employees(self, request, pk=None):

        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serilizer = EmployeeSerializer(emps, many=True, context={'request':request})
            return Response(emps_serilizer.data)
        except Exception as e:
            return Response({
                'massage' : 'Company might not Exist'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer