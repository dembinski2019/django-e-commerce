from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib import messages




class IndexView(TemplateView):

    template_name = 'core/index.html'



def contact(request):
    template = 'core/contact.html'
    sucess = False
    form =  ContactForm(request.POST or None )
    if form.is_valid():
        form.send_email()
        sucess = True
    elif request.method =='POST':
        messages.error(request,'Formulario inválido')
    context = {'form': form, 'sucess':sucess}
    return render(request,template, context)
    
