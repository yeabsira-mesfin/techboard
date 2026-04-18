from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('jobs/', include('jobs.urls', namespace='jobs')),
    path('applications/', include('applications.urls', namespace='applications')),
    path('', RedirectView.as_view(url='/jobs/', permanent=False)),  # ← add this
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)