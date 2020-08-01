from django.urls import path
from .views import (RegistrationView, IndexView,
                    UpdateUserView,UpdatePasswordView,
                    )
from django.contrib.auth.views import LoginView , LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('alterar-dados', UpdateUserView.as_view(), name='update_user'),
    path('alterar-senha', UpdatePasswordView.as_view(), name='update_password'),
    path('registro/', RegistrationView.as_view(), name='register'),
    path('entrar/',LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
]
