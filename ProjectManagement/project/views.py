from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from django.urls import reverse_lazy
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task, ProjectManager
from .forms import ProjectForm, TaskForm, ProjectProgressUpdateForm, TaskProgressUpdateForm

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project:project_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Project created successfully.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating the project. Please check the form and try again.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['form_errors'] = self.get_form().errors
        return context

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    success_url = reverse_lazy('project:project_list')

    def test_func(self):
        return self.request.user.is_staff

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'
    success_url = reverse_lazy('project:project_list')

    def test_func(self):
        return self.request.user.is_staff




class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'project/task_list.html'
    context_object_name = 'tasks'
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'project/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'project/task_form.html'

    def get_initial(self):
        initial = super().get_initial()
        project_id = self.request.GET.get('project')
        if project_id:
            initial['project'] = Project.objects.get(pk=project_id)
        return initial

    def get_success_url(self):
        if self.object.project:
            return reverse_lazy('project:project_detail', kwargs={'pk': self.object.project.pk})
        else:
            return reverse_lazy('project:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name', 'start_date', 'end_date', 'percent_complete', 'dependencies']
    template_name = 'project/task_form.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.project is None:
            raise Http404("Task has no associated project")
        return obj

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.object.project.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        return context
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'project/task_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.object.project.pk})

class ProjectTimelineView(LoginRequiredMixin, TemplateView):
    template_name = 'project/project_timeline.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['tasks'] = Task.objects.all()
        return context

def get_gantt_data(request):
    projects = Project.objects.all()
    data = []
    for project in projects:
        data.append({
            'pID': project.id,
            'pName': project.name,
            'pStart': project.start_date.strftime('%Y-%m-%d'),
            'pEnd': project.end_date.strftime('%Y-%m-%d'),
            'pClass': 'ggroupblack',
            'pLink': '',
            'pMile': 0,
            'pRes': '',
            'pComp': project.percent_complete,
            'pGroup': 1,
            'pParent': 0,
            'pOpen': 1,
            'pDepend': ''
        })
        for task in project.tasks.all():
            data.append({
                'pID': f"{project.id}-{task.id}",
                'pName': task.name,
                'pStart': task.start_date.strftime('%Y-%m-%d'),
                'pEnd': task.end_date.strftime('%Y-%m-%d'),
                'pClass': 'gtaskblue',
                'pLink': '',
                'pMile': 0,
                'pRes': '',
                'pComp': task.percent_complete,
                'pGroup': 0,
                'pParent': project.id,
                'pOpen': 1,
                'pDepend': ','.join([f"{project.id}-{dep.id}" for dep in task.dependencies.all()])
            })
    return JsonResponse(data, safe=False)

def update_task_progress(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        percent = request.POST.get('percent')
        if '-' in task_id:
            project_id, task_id = task_id.split('-')
            task = get_object_or_404(Task, id=task_id)
        else:
            task = get_object_or_404(Project, id=task_id)
        task.percent_complete = int(percent)
        task.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# If you have ProjectManager views, include them here
class ProjectManagerCreateView(LoginRequiredMixin, CreateView):
    model = ProjectManager
    fields = ['user', 'role']
    template_name = 'project/project_manager_form.html'

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.kwargs['project_pk']})

class ProjectManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectManager
    fields = ['user', 'role']
    template_name = 'project/project_manager_form.html'

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.object.project.pk})

class ProjectManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectManager
    template_name = 'project/project_manager_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('project:project_detail', kwargs={'pk': self.object.project.pk})