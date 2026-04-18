from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView
from accounts.mixins import SeekerRequiredMixin, EmployerRequiredMixin
from .models import Application
from .forms import ApplicationForm
from jobs.models import JobListing

# ── Seeker: Apply to a Job ─────────────────────────────────────────────────────
class ApplyView(SeekerRequiredMixin, ListView):
    template_name = 'applications/apply.html'

    def get(self, request, pk):
        job = get_object_or_404(JobListing, pk=pk, is_active=True)
        already_applied = Application.objects.filter(job=job, applicant=request.user).exists()
        form = ApplicationForm()
        return render(request, self.template_name, {
            'job': job, 'form': form, 'already_applied': already_applied
        })

    def post(self, request, pk):
        job = get_object_or_404(JobListing, pk=pk, is_active=True)
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, "Application submitted!")
            return redirect('applications:seeker_dashboard')
        return render(request, self.template_name, {'job': job, 'form': form})

# ── Seeker: Dashboard ──────────────────────────────────────────────────────────
class SeekerDashboardView(SeekerRequiredMixin, ListView):
    template_name = 'applications/seeker_dashboard.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)

# ── Employer: View Applicants ──────────────────────────────────────────────────
class ApplicantsListView(EmployerRequiredMixin, ListView):
    template_name = 'applications/applicants.html'
    context_object_name = 'applications'

    def get_queryset(self):
        job = get_object_or_404(JobListing, pk=self.kwargs['pk'], posted_by=self.request.user)
        return Application.objects.filter(job=job)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = get_object_or_404(JobListing, pk=self.kwargs['pk'])
        return context

# ── Employer: Update Applicant Status ─────────────────────────────────────────
def update_status(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(Application.STATUS_CHOICES):
            application.status = status
            application.save()
            messages.success(request, "Status updated!")
    return redirect('applications:applicants', pk=application.job.pk)