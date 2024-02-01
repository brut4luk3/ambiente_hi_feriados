from flask import request
from django.http import JsonResponse

def get_feriado_description(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        data_atual = request.POST.get('data_atual')

        api_url = 'https://ambientehiferiados-production.up.railway.app/api/check_holiday'

        response = request.post(api_url, json={'token': token, 'data_atual': data_atual})

        data = response.json()

        return JsonResponse(data)