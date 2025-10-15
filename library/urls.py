from django.contrib import admin
from django.urls import path
from library import views  # our app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # main homepage
]
