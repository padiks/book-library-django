from django.urls import path, re_path
from common import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Single smart route for everything under /book/
    re_path(r'^book/(?P<book_name>[^/]+)(?:/(?P<subpath>.*))?/$', views.book_index, name='book_index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
