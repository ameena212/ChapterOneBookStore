from django.views import generic
from django.contrib.auth.views import LoginView  
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationView(CreateView):  
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView): 
    template_name = 'registration/login.html'  
