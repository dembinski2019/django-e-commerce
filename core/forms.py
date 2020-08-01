from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = f'Nome: {name}\nE-mail: {email} \n{message} '
        send_mail(
            'Contato do Django E-Commerce', 
            message, settings.DEFAULT_FROM_EMAIL, 
            [settings.DEFAULT_FROM_EMAIL]
            )