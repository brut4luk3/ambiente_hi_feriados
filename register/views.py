from django.shortcuts import render

from users.models import CustomUser


def new(request):

    if request.method == 'GET':

        return render(request, 'register/new.html')

    elif request.method == 'POST':

        post_data = request.POST

        u = CustomUser(
            email=post_data.get('email'),
            password=post_data.get('password'),
            first_name=post_data.get('name'),
            last_name=post_data.get('lastname')
        )

        u.set_password(post_data.get("password"))
        u.save()

        return render(request, 'register/success.html')