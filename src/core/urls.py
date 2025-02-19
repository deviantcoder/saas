from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view), # home page -> root page
    path('hello-world/', views.home_view),
    path('about/', views.about_view),
]
