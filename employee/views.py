from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView
from .serializers import EmployeeSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Employee

# Create your views here.

class EmployeeGetCreateAPIView(APIView):
    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializers(employee, many=True)
        return Response({"message": "all employee", "date": serializer.data}, status=status.HTTP_200_OK)
    
    
    def post(self, request, format=None):
        serializer = EmployeeSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "employee create successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    
    
class EmployeeModifyAPIView(APIView):
    def patch(self, request, pk, format=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializers(employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "employee data update successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response({"message": "delete employee data"}, status=status.HTTP_200_OK)