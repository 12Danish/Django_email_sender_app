from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomRegistrationForm


# Redirects user to homepage
class HomepageView(TemplateView):
    template_name = 'users/homepage.html'


# Handles the login functionality
class CustomLoginView(LoginView):
    template_name = 'users/login.html'


# Handles the registration View
class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('users:login')
