from django.urls import path
from .views import EmployeeGetCreateAPIView, EmployeeModifyAPIView

urlpatterns =[
    path("employees/", EmployeeGetCreateAPIView.as_view(), name="create_employee"),
    path("employees/<int:pk>/", EmployeeModifyAPIView.as_view(), name="update_delete_employee")
]