from django.urls import path
from .views import HomepageView, CustomLoginView, RegistrationView, CustomLogoutView
from django.contrib.auth.views import LogoutView

app_name = 'users'

# Defining urls for creating users and handling authentications
urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('registration', RegistrationView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout')
]
