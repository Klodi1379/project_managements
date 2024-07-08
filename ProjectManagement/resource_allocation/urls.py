from django.urls import path
from . import views

app_name = 'resource_allocation'

urlpatterns = [
    path('', views.AllocationListView.as_view(), name='allocation_list'),
    
    path('material/create/', views.MaterialAllocationCreateView.as_view(), name='material_allocation_create'),
    path('material/<int:pk>/update/', views.MaterialAllocationUpdateView.as_view(), name='material_allocation_update'),
    path('material/<int:pk>/delete/', views.MaterialAllocationDeleteView.as_view(), name='material_allocation_delete'),
    
    path('equipment/create/', views.EquipmentAllocationCreateView.as_view(), name='equipment_allocation_create'),
    path('equipment/<int:pk>/update/', views.EquipmentAllocationUpdateView.as_view(), name='equipment_allocation_update'),
    path('equipment/<int:pk>/delete/', views.EquipmentAllocationDeleteView.as_view(), name='equipment_allocation_delete'),
    
    path('employee/create/', views.EmployeeAllocationCreateView.as_view(), name='employee_allocation_create'),
    path('employee/<int:pk>/update/', views.EmployeeAllocationUpdateView.as_view(), name='employee_allocation_update'),
    path('employee/<int:pk>/delete/', views.EmployeeAllocationDeleteView.as_view(), name='employee_allocation_delete'),
]