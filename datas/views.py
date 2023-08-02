from django.shortcuts import render, redirect, get_object_or_404
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

def selecionar_feriados(request):
    feriados_cadastrados = request.user.feriados_set.all()

    context = {
        'feriados_cadastrados': feriados_cadastrados
    }

    return render(request, 'deletar/selecionar_feriados.html', context=context)

def deletar_feriados(request, feriados_id):
    if request.method == 'GET':

        feriado = get_object_or_404(Feriados, pk=feriados_id)

        context = {
            'feriado': feriado
        }

        return render(request, 'deletar/deletar_feriados.html', context=context)

    elif request.method == 'POST':

        feriado_excluido = Feriados.objects.filter(id=feriados_id).delete()

        return render(request, 'deletar/sucesso_deletar.html')

def deletar_todas(request):
    if request.method == 'GET':

        feriados_set = Feriados.objects.all()

        context = {
            'feriados_set': feriados_set
        }

        return render(request, 'deletar/deletar_todas.html', context=context)

    elif request.method == 'POST':

        feriados_excluidos = Feriados.objects.all().delete()

        return render(request, 'deletar/sucesso_deletar.html')

def editar_feriados(request, feriados_id):
    if request.method == 'GET':

        feriado = get_object_or_404(Feriados, pk=feriados_id)

        context = {
            'feriado': feriado
        }

        return render(request, 'editar/editar_feriados.html', context=context)

    elif request.method == 'POST':

        feriado_editado = Feriados.objects.filter(id=feriados_id).update()

        return render(request, 'editar/editar_feriados.html')