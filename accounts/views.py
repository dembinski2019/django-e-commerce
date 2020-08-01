from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import (CreateView,TemplateView,
                                UpdateView,FormView,
                                )
from django.urls import reverse_lazy
from .forms import UserAdminCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm



User = get_user_model()

class IndexView(LoginRequiredMixin,TemplateView):
    
    template_name = 'accounts/index.html'
    

class RegistrationView(CreateView):

    form_class =UserAdminCreationForm
    template_name = 'accounts/register.html'
    model = User
    success_url = reverse_lazy('index')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields=['name', 'email']
    success_url=reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user
    

class UpdatePasswordView(LoginRequiredMixin,FormView):
    
    template_name = 'accounts/update_password.html'
    success_url=reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs=super(UpdatePasswordView,self).get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs

    def form_valid(self,form):
        form.save()
        return super(UpdatePasswordView,self).form_valid(form)