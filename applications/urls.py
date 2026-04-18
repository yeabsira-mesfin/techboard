from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:pk>/', views.ApplyView.as_view(), name='apply'),
    path('dashboard/', views.SeekerDashboardView.as_view(), name='seeker_dashboard'),
    path('job/<int:pk>/applicants/', views.ApplicantsListView.as_view(), name='applicants'),
    path('status/<int:pk>/', views.update_status, name='update_status'),
]