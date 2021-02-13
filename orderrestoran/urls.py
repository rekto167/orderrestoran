from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static

from .views import IndexView, AboutView

urlpatterns = [
    path('restoran/', include('restoran.urls', namespace='restoran')),
    path('about/', AboutView.as_view(), name='about'),
    path('', IndexView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
