from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class EmployerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.profile.role != 'employer':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class SeekerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.profile.role != 'seeker':
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)