from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from datas.models import Feriados

def cadastrar_feriados(request):
    if request.method == 'GET':

        return render(request, 'cadastrar/cadastrar_feriados.html')

    elif request.method == 'POST':

        post_data = request.POST
        f = Feriados(
            usuario=request.user,
            data=post_data.get('data'),
            description=post_data.get('description')
        )

        f.save()

        messages.success(request, 'Nova data cadastrada com sucesso!')

        return redirect(reverse('datas:cadastrar_feriados'))

def deletar_feriados(request):

    return render(request, 'deletar/deletar_feriados.html')