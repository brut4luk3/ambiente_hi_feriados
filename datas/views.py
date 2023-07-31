from django.shortcuts import render
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

        return render(request, 'cadastrar/cadastrar_feriados.html')

def deletar_feriados(request):

    return render(request, 'deletar/deletar_feriados.html')