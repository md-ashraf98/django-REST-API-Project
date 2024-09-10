# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    path('test/', lambda request: HttpResponse("Test page")),  # For testing
]

