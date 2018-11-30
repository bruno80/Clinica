from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cliente/', views.list_cliente),
    path('medico/', views.list_medico),
    path('cliente/<int:cliente_id>/',views.cliente_show),
    path('medico/<int:medico_id>/',views.medico_show)
]