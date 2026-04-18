from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .models import JobListing
from .forms import JobListingForm
from accounts.mixins import EmployerRequiredMixin, SeekerRequiredMixin

# ── Public: Job Listings with search/filter ────────────────────────────────────
class JobListingView(ListView):
    model = JobListing
    template_name = 'jobs/listing.html'
    context_object_name = 'jobs'
    paginate_by = 10

    def get_queryset(self):
        qs = JobListing.objects.filter(is_active=True)
        q = self.request.GET.get('q')
        job_type = self.request.GET.get('job_type')
        stack = self.request.GET.get('stack')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if job_type:
            qs = qs.filter(job_type=job_type)
        if stack:
            qs = qs.filter(tech_stack__icontains=stack)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_types'] = JobListing.JOB_TYPE_CHOICES
        return context

# ── Public: Job Detail ─────────────────────────────────────────────────────────
class JobDetailView(DetailView):
    model = JobListing
    template_name = 'jobs/detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_tags'] = [t.strip() for t in self.object.tech_stack.split(',') if t.strip()]
        return context

# ── Employer: Post a Job ───────────────────────────────────────────────────────
class JobCreateView(EmployerRequiredMixin, CreateView):
    model = JobListing
    form_class = JobListingForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('jobs:employer_dashboard')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, "Job posted successfully!")
        return super().form_valid(form)

# ── Employer: Edit a Job ───────────────────────────────────────────────────────
class JobUpdateView(EmployerRequiredMixin, UpdateView):
    model = JobListing
    form_class = JobListingForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('jobs:employer_dashboard')

    def get_queryset(self):
        return JobListing.objects.filter(posted_by=self.request.user)

# ── Employer: Delete a Job ─────────────────────────────────────────────────────
class JobDeleteView(EmployerRequiredMixin, DeleteView):
    model = JobListing
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('jobs:employer_dashboard')

    def get_queryset(self):
        return JobListing.objects.filter(posted_by=self.request.user)

# ── Employer: Dashboard ────────────────────────────────────────────────────────
class EmployerDashboardView(EmployerRequiredMixin, ListView):
    model = JobListing
    template_name = 'jobs/employer_dashboard.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return JobListing.objects.filter(posted_by=self.request.user)