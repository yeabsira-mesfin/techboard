from django import forms
from .models import JobListing

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = [
            'title', 'company', 'description', 'requirements',
            'salary_min', 'salary_max', 'job_type', 'tech_stack', 'is_active'
        ]