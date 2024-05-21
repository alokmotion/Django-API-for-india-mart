from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch-leads/', views.fetch_leads, name='fetch_leads'),
]
