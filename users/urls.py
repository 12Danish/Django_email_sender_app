from django.urls import path
from .views import HomepageView, CustomLoginView, RegistrationView, CustomLogoutView

app_name = 'users'

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('logout', CustomLogoutView.as_view(), name='logout')
]
