from django import forms
from .models import JobListing

INPUT_CLASS = "w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = [
            'title', 'company', 'description', 'requirements',
            'salary_min', 'salary_max', 'job_type', 'tech_stack', 'is_active'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'company': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 5}),
            'requirements': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 4}),
            'salary_min': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'salary_max': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'job_type': forms.Select(attrs={'class': INPUT_CLASS}),
            'tech_stack': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'is_active': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-indigo-600'}),
        }