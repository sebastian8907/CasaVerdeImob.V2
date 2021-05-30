from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def user_create(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        passwd = request.POST.get('passwd', '')
        passwd2 = request.POST.get('passwd2', '')

        if passwd == passwd2:
            if len(passwd) >= 6:
                try:
                    user = User.objects.create_user(username=email, email=email, password=passwd)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                except IntegrityError:
                    return render(request, 'registration/user_create.html',
                                  {'error': 'Exista deja un cont cu aceasta adresa de e-mail!'})
            else:
                return render(request, 'registration/user_create.html',
                              {'error': 'Parola trebuie sa contina minim 6 caractere'})
        elif passwd != passwd2:
            return render(request, 'registration/user_create.html',
                          {'error': 'Parolele nu se potrivesc.'})
        return redirect('homepage')

    is_logged_in = request.user is not None and not request.user.is_anonymous
    return render(request, 'registration/user_create.html',
                  {'user_create': user_create, 'submit_text': 'Creaza cont', 'is_logged_in': is_logged_in})


def term_cond(request):
    context = {}
    return render(request, 'registration/termeni_conditii.html', context)


def gdpr(request):
    context = {}
    return render(request, 'registration/GDPR.html', context)
