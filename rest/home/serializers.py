from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from home.models import Employees

class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model =Employees
        fields=('firstname','lastname')