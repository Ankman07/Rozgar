from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('registration/', views.registration_portal, name='registration_portal'),  # Template rendering
    path('api/register-laborer/', views.register_laborer, name='register_laborer'),  # API endpoint
    path('api/register-contractor/', views.register_contractor, name='register_contractor'),  # API endpoint
]
