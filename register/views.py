from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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

def validate_email(request):

    if request.method == 'GET':

        return render(request, 'change_password/validate_email.html')

    elif request.method == 'POST':

        post_data_validate_email = request.POST
        forms_email_validate_email = post_data_validate_email.get('validateemail')

        if CustomUser.objects.filter(email=forms_email_validate_email).exists():

            user = get_object_or_404(CustomUser, email=forms_email_validate_email)
            request.session['user_token'] = str(user.token)

            return redirect(reverse('register:change_password'))

        else:

            unknown_email = {
                'unknown_email': _('Este e-mail não existe em nossa base de dados!')
            }
            return render(request, 'change_password/validate_email.html', {'unknown_email': unknown_email})

def change_password(request):
    user_token = request.session.get('user_token')
    user = get_object_or_404(CustomUser, token=user_token)

    if request.method == 'GET':

        return render(request, 'change_password/change_password.html')

    elif request.method == 'POST':

        password = request.POST.get('changepassword')
        new_password = request.POST.get('changepasswordconfirm')

        if password != new_password:
            password_errors = {
                'unequal_password': _('As senhas não conferem!')
            }
            return render(request, 'change_password/change_password.html', {'password_errors': password_errors})

        else:

            user.set_password(new_password)
            user.save()

            del request.session['user_token']

            return render(request, 'change_password/success_change_password.html')