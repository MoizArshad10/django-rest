from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from home import views

urlpatterns = [
    path("" , views.emp_list.as_view() , name='emp_list')
]