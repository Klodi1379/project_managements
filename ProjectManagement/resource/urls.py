from django.urls import path
from . import views

app_name = 'resource'

urlpatterns = [
    # Material URLs
    path('materials/', views.MaterialListView.as_view(), name='material_list'),
    path('materials/<int:pk>/', views.MaterialDetailView.as_view(), name='material_detail'),
    path('materials/create/', views.MaterialCreateView.as_view(), name='material_create'),
    path('materials/<int:pk>/update/', views.MaterialUpdateView.as_view(), name='material_update'),
    path('materials/<int:pk>/delete/', views.MaterialDeleteView.as_view(), name='material_delete'),

    # Equipment URLs
    path('equipment/', views.EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/create/', views.EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/update/', views.EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', views.EquipmentDeleteView.as_view(), name='equipment_delete'),

    # Craft URLs
    path('crafts/', views.CraftListView.as_view(), name='craft_list'),
    path('crafts/<int:pk>/', views.CraftDetailView.as_view(), name='craft_detail'),
    path('crafts/create/', views.CraftCreateView.as_view(), name='craft_create'),
    path('crafts/<int:pk>/update/', views.CraftUpdateView.as_view(), name='craft_update'),
    path('crafts/<int:pk>/delete/', views.CraftDeleteView.as_view(), name='craft_delete'),

    # SubContractor URLs
    path('subcontractors/', views.SubContractorListView.as_view(), name='subcontractor_list'),
    path('subcontractors/<int:pk>/', views.SubContractorDetailView.as_view(), name='subcontractor_detail'),
    path('subcontractors/create/', views.SubContractorCreateView.as_view(), name='subcontractor_create'),
    path('subcontractors/<int:pk>/update/', views.SubContractorUpdateView.as_view(), name='subcontractor_update'),
    path('subcontractors/<int:pk>/delete/', views.SubContractorDeleteView.as_view(), name='subcontractor_delete'),
]