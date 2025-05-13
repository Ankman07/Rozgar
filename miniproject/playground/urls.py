from django.urls import path
from . import views
urlpatterns=[
    path('hello/',views.say_hello),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('registration/',views.registration,name='registration'),
    path('notification/',views.notification,name='notification'),
    path('admin',views.admin,name='admin')
] 

