from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import User, Employee
from .forms import CustomUserCreationForm, CustomUserChangeForm, EmployeeForm

class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'employee_management/user_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_staff

class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'employee_management/user_detail.html'
    context_object_name = 'user'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.pk == self.kwargs['pk']

class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'employee_management/user_form.html'
    success_url = reverse_lazy('user_list')

    def test_func(self):
        return self.request.user.is_staff

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'employee_management/user_form.html'
    success_url = reverse_lazy('user_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.pk == self.kwargs['pk']

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'employee_management/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def test_func(self):
        return self.request.user.is_staff

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_management/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee_management/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_management/employee_form.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_staff

class EmployeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_management/employee_form.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_staff

class EmployeeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employee
    template_name = 'employee_management/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_staff

# Additional view for user profile
class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'employee_management/user_profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user