from django.urls import path

from datas import views

app_name = 'datas'

urlpatterns =[
    path('cadastrar/', views.cadastrar_feriados, name='cadastrar_feriados'),
    path('deletar/', views.deletar_feriados, name='deletar_feriados'),
]