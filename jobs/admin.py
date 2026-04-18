from django.contrib import admin
from .models import JobListing

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'job_type', 'is_active', 'posted_by', 'posted_at']
    list_filter = ['job_type', 'is_active']
    search_fields = ['title', 'company', 'tech_stack']
    list_editable = ['is_active']