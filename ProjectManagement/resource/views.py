from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Material, Equipment, Craft, SubContractor
from .forms import MaterialForm, EquipmentForm, CraftForm, SubContractorForm

# Material Views
class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    template_name = 'resource/material_list.html'
    context_object_name = 'materials'

class MaterialDetailView(LoginRequiredMixin, DetailView):
    model = Material
    template_name = 'resource/material_detail.html'
    context_object_name = 'material'

class MaterialCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'resource/material_form.html'
    success_url = reverse_lazy('resource:material_list')

    def test_func(self):
        return self.request.user.is_staff

class MaterialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'resource/material_form.html'
    success_url = reverse_lazy('resource:material_list')

    def test_func(self):
        return self.request.user.is_staff

class MaterialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Material
    template_name = 'resource/material_confirm_delete.html'
    success_url = reverse_lazy('resource:material_list')

    def test_func(self):
        return self.request.user.is_staff

# Equipment Views
class EquipmentListView(LoginRequiredMixin, ListView):
    model = Equipment
    template_name = 'resource/equipment_list.html'
    context_object_name = 'equipment'

class EquipmentDetailView(LoginRequiredMixin, DetailView):
    model = Equipment
    template_name = 'resource/equipment_detail.html'
    context_object_name = 'equipment'

class EquipmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'resource/equipment_form.html'
    success_url = reverse_lazy('resource:equipment_list')

    def test_func(self):
        return self.request.user.is_staff

class EquipmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'resource/equipment_form.html'
    success_url = reverse_lazy('resource:equipment_list')

    def test_func(self):
        return self.request.user.is_staff

class EquipmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Equipment
    template_name = 'resource/equipment_confirm_delete.html'
    success_url = reverse_lazy('resource:equipment_list')

    def test_func(self):
        return self.request.user.is_staff

# Craft Views
class CraftListView(LoginRequiredMixin, ListView):
    model = Craft
    template_name = 'resource/craft_list.html'
    context_object_name = 'crafts'

class CraftDetailView(LoginRequiredMixin, DetailView):
    model = Craft
    template_name = 'resource/craft_detail.html'
    context_object_name = 'craft'

class CraftCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Craft
    form_class = CraftForm
    template_name = 'resource/craft_form.html'
    success_url = reverse_lazy('resource:craft_list')

    def test_func(self):
        return self.request.user.is_staff

class CraftUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Craft
    form_class = CraftForm
    template_name = 'resource/craft_form.html'
    success_url = reverse_lazy('resource:craft_list')

    def test_func(self):
        return self.request.user.is_staff

class CraftDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Craft
    template_name = 'resource/craft_confirm_delete.html'
    success_url = reverse_lazy('resource:craft_list')

    def test_func(self):
        return self.request.user.is_staff

# SubContractor Views
class SubContractorListView(LoginRequiredMixin, ListView):
    model = SubContractor
    template_name = 'resource/subcontractor_list.html'
    context_object_name = 'subcontractors'

class SubContractorDetailView(LoginRequiredMixin, DetailView):
    model = SubContractor
    template_name = 'resource/subcontractor_detail.html'
    context_object_name = 'subcontractor'

class SubContractorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = SubContractor
    form_class = SubContractorForm
    template_name = 'resource/subcontractor_form.html'
    success_url = reverse_lazy('resource:subcontractor_list')

    def test_func(self):
        return self.request.user.is_staff

class SubContractorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SubContractor
    form_class = SubContractorForm
    template_name = 'resource/subcontractor_form.html'
    success_url = reverse_lazy('resource:subcontractor_list')

    def test_func(self):
        return self.request.user.is_staff

class SubContractorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SubContractor
    template_name = 'resource/subcontractor_confirm_delete.html'
    success_url = reverse_lazy('resource:subcontractor_list')

    def test_func(self):
        return self.request.user.is_staff