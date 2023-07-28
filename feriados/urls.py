from django.urls import path

from . import views

app_name = 'feriados'

urlpatterns =[
    path('', views.cadastrar_feriados, name='cadastrar_feriados'),
]