import imp
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employees
from . serializers import EmployeesSerializer

class emp_list(APIView):

    def get(self,request):
        emp_one = Employees.objects.all()
        serializer = EmployeesSerializer(emp_one, many = True)
        return Response(serializer.data)