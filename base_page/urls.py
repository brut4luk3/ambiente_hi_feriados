from django.urls import path

from . import views

app_name = 'base_page'

urlpatterns =[
    path('', views.base_page, name='base_page_redirect')
]