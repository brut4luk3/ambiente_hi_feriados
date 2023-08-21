from django.urls import path
from . import views

app_name = 'api_view'

urlpatterns = [
    path('api/get_feriado_description/', views.get_feriado_description, name='get_feriado_description'),
]
