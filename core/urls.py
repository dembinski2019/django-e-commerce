from django.urls import path
from .views import  contact, IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', contact, name='contact'),
    
]
