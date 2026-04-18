from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter', 'resume']

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if not resume.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
            if resume.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File size must be under 5MB.")
        return resume