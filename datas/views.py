from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from datas.models import Feriados
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.utils import timezone

def cadastrar_feriados(request):
    if request.method == 'GET':

        return render(request, 'cadastrar/cadastrar_feriados.html')

    elif request.method == 'POST':

        post_data = request.POST
        informed_date = post_data.get('data')

        informed_datetime = datetime.strptime(informed_date, '%Y-%m-%d')

        current_year = timezone.now().year

        updated_date = informed_datetime.replace(year=current_year)

        if Feriados.objects.filter(data=informed_date).exists():
            date_error = {
                'equal_date': _('Esta data já foi cadastrada neste banco de dados!')
            }
            return render(request, 'cadastrar/cadastrar_feriados.html', {'date_error': date_error})
        else:

            f = Feriados(
                usuario=request.user,
                data=updated_date,
                description=post_data.get('description')
            )

            f.save()

            messages.success(request, 'Nova data cadastrada com sucesso!')

            return redirect(reverse('datas:cadastrar_feriados'))

def selecionar_feriados(request):
    feriados_cadastrados = request.user.feriados_set.all()
    quantidade_datas = feriados_cadastrados.count()

    context = {
        'feriados_cadastrados': feriados_cadastrados,
        'quantidade_datas': quantidade_datas
    }

    return render(request, 'deletar/selecionar_feriados.html', context=context)

def deletar_feriados(request, feriados_id):
    feriados_cadastrados = request.user.feriados_set.all()
    quantidade_datas = feriados_cadastrados.count()

    if request.method == 'GET':

        feriado = get_object_or_404(Feriados, pk=feriados_id)

        context = {
            'feriado': feriado,
            'quantidade_datas': quantidade_datas
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

        post_data_edit = request.POST

        form_id_dataedit = request.POST['dataedit']
        form_id_descriptionedit = request.POST['descriptionedit']

        feriado_editado = Feriados.objects.filter(id=feriados_id).update(data=form_id_dataedit, description=form_id_descriptionedit)

        return render(request, 'editar/sucesso_editar.html')