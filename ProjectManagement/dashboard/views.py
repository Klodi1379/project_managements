from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from project.models import Project
from resource.models import Material, Equipment, Craft, SubContractor
from django.db.models import Sum, Count
from django.utils import timezone

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Projects overview
        context['total_projects'] = Project.objects.count()
        context['ongoing_projects'] = Project.objects.filter(status='ONGOING').count()
        context['completed_projects'] = Project.objects.filter(status='COMPLETED').count()
        
        # Resources overview
        context['total_materials'] = Material.objects.count()
        context['total_equipment'] = Equipment.objects.count()
        context['total_crafts'] = Craft.objects.count()
        context['total_subcontractors'] = SubContractor.objects.count()
        
        # Project progress data for chart
        projects = Project.objects.all()
        project_names = [project.name for project in projects]
        project_progress = [project.progress_percentage for project in projects]
        context['project_names'] = project_names
        context['project_progress'] = project_progress
        
        # Resource allocation data for chart
        resource_types = ['Materials', 'Equipment', 'Crafts', 'Subcontractors']
        resource_counts = [
            context['total_materials'],
            context['total_equipment'],
            context['total_crafts'],
            context['total_subcontractors']
        ]
        context['resource_types'] = resource_types
        context['resource_counts'] = resource_counts
        
        return context