from django.urls import path
from .views import DashboardView, DraftsView, UpdateMailView,delete_mail, WriteMail, MailDetailsView

app_name = 'email_functionality'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('write_mail/', WriteMail.as_view(), name='write_mail'),
    path('delete_mail/<int:pk>',delete_mail, name='delete'),
    path('update_mail/<int:pk>', UpdateMailView.as_view(), name='update'),
    path('details/<int:pk>/', MailDetailsView.as_view(), name='details'),
    path('drafts/', DraftsView.as_view(), name='drafts')
]
# Create your views here.
