from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cliente/', views.list_cliente),
    path('medico/', views.list_medico)
]