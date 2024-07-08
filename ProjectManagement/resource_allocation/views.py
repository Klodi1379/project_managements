from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import MaterialAllocation, EquipmentAllocation, EmployeeAllocation
from .forms import MaterialAllocationForm, EquipmentAllocationForm, EmployeeAllocationForm

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class AllocationListView(LoginRequiredMixin, ListView):
    template_name = 'resource_allocation/allocation_list.html'
    context_object_name = 'allocations'
    
    def get_queryset(self):
        return[]
    
   


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['material_allocations'] = MaterialAllocation.objects.all()
        context['equipment_allocations'] = EquipmentAllocation.objects.all()
        context['employee_allocations'] = EmployeeAllocation.objects.all()
        return context

class MaterialAllocationCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = MaterialAllocation
    form_class = MaterialAllocationForm
    template_name = 'resource_allocation/allocation_form.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Material allocation created successfully.')
        return response

class MaterialAllocationUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = MaterialAllocation
    form_class = MaterialAllocationForm
    template_name = 'resource_allocation/allocation_form.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Material allocation updated successfully.')
        return response

class MaterialAllocationDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = MaterialAllocation
    template_name = 'resource_allocation/allocation_confirm_delete.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Material allocation deleted successfully.')
        return response

class EquipmentAllocationCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = EquipmentAllocation
    form_class = EquipmentAllocationForm
    template_name = 'resource_allocation/allocation_form.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Equipment allocation created successfully.')
        return response

class EquipmentAllocationUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = EquipmentAllocation
    form_class = EquipmentAllocationForm
    template_name = 'resource_allocation/allocation_form.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Equipment allocation updated successfully.')
        return response

class EquipmentAllocationDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = EquipmentAllocation
    template_name = 'resource_allocation/allocation_confirm_delete.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Equipment allocation deleted successfully.')
        return response

class EmployeeAllocationCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = EmployeeAllocation
    form_class = EmployeeAllocationForm
    template_name = 'resource_allocation/allocation_form.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Employee allocation created successfully.')
        return response

class EmployeeAllocationUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = EmployeeAllocation
    form_class = EmployeeAllocationForm
    template_name = 'resource_allocation/allocation_form.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Employee allocation updated successfully.')
        return response

class EmployeeAllocationDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = EmployeeAllocation
    template_name = 'resource_allocation/allocation_confirm_delete.html'
    success_url = reverse_lazy('resource_allocation:allocation_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Employee allocation deleted successfully.')
        return response