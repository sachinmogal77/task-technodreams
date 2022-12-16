from django.urls import path
from .views import EmployeeAPI,SignUpAPI,EmployeeDetailsApi

urlpatterns = [
    path('emp/',EmployeeAPI.as_view()),
     path('emp/<int:pk>/',EmployeeDetailsApi.as_view()),
    path('signup/',SignUpAPI.as_view())
]