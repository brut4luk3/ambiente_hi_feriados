from django.shortcuts import render

from users.models import CustomUser
from django.utils.translation import gettext_lazy as _

def new(request):

    if request.method == 'GET':

        return render(request, 'register/new.html')

    elif request.method == 'POST':

        post_data = request.POST
        forms_email = post_data.get('email')
        forms_password = post_data.get('password')
        forms_passwordconfirm = post_data.get('passwordconfirm')

        if CustomUser.objects.filter(email=forms_email).exists():
            email_errors = {
                'unique_email': _('Este e-mail já está sendo utilizado!')
            }
            return render(request, 'register/new.html', {'email_errors': email_errors})

        elif forms_password != forms_passwordconfirm:
            password_errors = {
                'unequal_password': _('As senhas não conferem!')
            }
            return render(request, 'register/new.html', {'password_errors': password_errors})

        else:
            u = CustomUser(
                email=post_data.get('email'),
                password=post_data.get('password'),
                first_name=post_data.get('name'),
                last_name=post_data.get('lastname')
            )
            u.set_password(post_data.get("password"))
            u.save()

            return render(request, 'register/success.html')

    return render(request, 'register/success.html')