from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import View

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'auth/logout.html')
    
    def post(self, request):
        logout(request)
        return render(request, 'auth/logout.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('employee-management/', include('employee_management.urls', namespace='employee_management')),
    path('company/', include('company.urls', namespace='company')),
    path('project/', include('project.urls', namespace='project')),
    path('resource/', include('resource.urls', namespace='resource')),
    path('resource-allocation/', include('resource_allocation.urls', namespace='resource_allocation')),

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html', next_page='dashboard:dashboard'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    
    # ... other URL patterns ...
]

urlpatterns += [
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='auth/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='auth/password_change_done.html'), name='password_change_done'),
]