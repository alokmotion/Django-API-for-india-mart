from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),  # This line includes the URLs from the leads app
]
