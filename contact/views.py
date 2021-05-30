from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        contact_us = ContactForm()
    else:
        contact_us = ContactForm(request.POST)
        if contact_us.is_valid():
            phone = contact_us.cleaned_data['phone']
            from_email = contact_us.cleaned_data['from_email']
            message = contact_us.cleaned_data['message']
            name = contact_us.cleaned_data['name']
            try:
                send_mail(name, 'De la: ' + from_email + '\n' + 'Tel: ' + str(phone) + '\n' + 'Mesaj:' + '\n' + message,
                          from_email, ['sebastian.albu.sa@gmail.com'],
                          fail_silently=False, auth_user=None, auth_password=None)
            except BadHeaderError:
                return HttpResponse('A aparut o eroare! Incearca din nou.')
    return render(request, "contact/email.html", {'form': contact_us})
