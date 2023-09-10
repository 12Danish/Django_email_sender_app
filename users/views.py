from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Create your views here.
class HomepageView(TemplateView):
    template_name = 'users/homepage.html'


class CustomLoginView(LoginView):
    template_name = 'users/template.html'


class CustomLogoutView(LogoutView):
    pass


class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
