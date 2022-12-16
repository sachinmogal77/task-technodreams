from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializations import EmployeeSerializer,SignUpSerializer,User
from .models import Employee
from rest_framework.permissions import IsAuthenticated

class EmployeeAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailsApi(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            data = {"msg":"The Resourse You looking for does not exist"}
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk):
            try:
                employee = Employee.objects.get(pk=pk)
                employee.delete()
                return Response(data={"msg":"No Content"},status=status.HTTP_204_NO_CONTENT)
            except Employee.DoesNotExist:
                data = {"msg":"The Resourse You looking for does not exist"}
                return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
            try:
                employee = Employee.objects.get(pk=pk)
                serializer = EmployeeSerializer(data=request.data,instance=employee,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except Employee.DoesNotExist:
                data = {"msg":"The Resourse You looking for does not exist"}
                return Response(data=data,status=status.HTTP_404_NOT_FOUND)


class SignUpAPI(APIView):
    def post(self,request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

