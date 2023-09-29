from django.shortcuts import render
from users.forms import CustomAuthenticationForm

def login(request):

    form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def index(request):

    if request.user.is_authenticated:
        listar_datas = request.user.feriados_set.all()
        quantidade_datas = listar_datas.count()

        context = {
            'listar_datas': listar_datas,
            'quantidade_datas': quantidade_datas
        }

        return render(request, 'inicio/index.html', context=context)

    else:

        return render(request, 'inicio/index.html')