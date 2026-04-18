from django.db import models
from django.contrib.auth.models import User

class JobListing(models.Model):
    JOB_TYPE_CHOICES = [
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('onsite', 'On-site'),
    ]
    def get_tech_tags(self):
        return [tag.strip() for tag in self.tech_stack.split(',') if tag.strip()]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)
    tech_stack = models.CharField(max_length=300, blank=True, help_text="Comma-separated, e.g. Python, React, Docker")
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listings')
   

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-posted_at']
    