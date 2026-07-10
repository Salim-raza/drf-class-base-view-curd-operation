from django.urls import path
from .views import EmployeeGetCreateAPIView, EmployeeModifyAPIView, EmployeeSearch

urlpatterns =[
    path("employees/", EmployeeGetCreateAPIView.as_view(), name="create_employee"),
    path("employees/<int:pk>/", EmployeeModifyAPIView.as_view(), name="update_delete_employee"),
    path("search/", EmployeeSearch.as_view(), name="employee_search")
]