from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobListingView.as_view(), name='listing'),
    path('<int:pk>/', views.JobDetailView.as_view(), name='detail'),
    path('post/', views.JobCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.JobUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.JobDeleteView.as_view(), name='delete'),
    path('dashboard/', views.EmployerDashboardView.as_view(), name='employer_dashboard'),
]