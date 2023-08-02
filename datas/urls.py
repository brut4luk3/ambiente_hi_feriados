from django.urls import path

from datas import views

app_name = 'datas'

urlpatterns =[
    path('cadastrar/', views.cadastrar_feriados, name='cadastrar_feriados'),
    path('selecionar/', views.selecionar_feriados, name='selecionar_feriados'),
    path('deletar/<int:feriados_id>/', views.deletar_feriados, name='deletar_feriados'),
    path('deletar/todas/', views.deletar_todas, name='deletar_todas'),
    path('editar/<int:feriados_id>/', views.editar_feriados, name='editar_feriados'),
]