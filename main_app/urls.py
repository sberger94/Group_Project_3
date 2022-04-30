from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views 

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('patients/', views.patients_index, name='patients'),
   path('patients/<int:patient_id>/', views.patient_history, name='patient_history'),
]