from django.urls import path

from . import views


app_name = 'register'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('validate_email/', views.validate_email, name='validate_email'),
    path('change_password/', views.change_password, name='change_password'),
]