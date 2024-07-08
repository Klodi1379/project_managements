from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    # Project URLs
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    
    # Task URLs
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    
    # Project Timeline
    path('timeline/', views.ProjectTimelineView.as_view(), name='project_timeline'),
    
    # API endpoints for Gantt chart
    path('api/gantt-data/', views.get_gantt_data, name='gantt_data'),
    path('api/update-progress/', views.update_task_progress, name='update_progress'),
    
    # Project Manager URLs (if you have these views)
    path('<int:project_pk>/manager/add/', views.ProjectManagerCreateView.as_view(), name='project_manager_create'),
    path('manager/<int:pk>/update/', views.ProjectManagerUpdateView.as_view(), name='project_manager_update'),
    path('manager/<int:pk>/delete/', views.ProjectManagerDeleteView.as_view(), name='project_manager_delete'),
]