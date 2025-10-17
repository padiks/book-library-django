from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Main URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),  # include all app routes
]

# Serve static files when DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom 404 handler
handler404 = 'common.views.handler404'
