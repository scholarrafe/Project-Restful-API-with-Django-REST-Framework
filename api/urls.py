
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers

from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(f'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
