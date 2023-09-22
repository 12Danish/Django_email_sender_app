from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import WriteMailForm
from .models import Mails
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'email_functionality/dashboard.html'
    context_object_name = 'emails'

    def get_queryset(self):
        user = self.request.user
        return Mails.objects.filter(user=user)


class DraftsView(LoginRequiredMixin, ListView):
    pass


class MailDetailsView(LoginRequiredMixin, DetailView):
    model = Mails
    template_name = 'email_functionality/mail_details.html'
    context_object_name = 'mail'

class WriteMail(LoginRequiredMixin, FormView):
    template_name = 'email_functionality/write_mail.html'
    form_class = WriteMailForm

    def form_valid(self, form):
        data = form.cleaned_data
        Mails.objects.create(user=self.request.user,
                             subject=data['subject'],
                             recipient=data['recipient'],
                             body=data['body'],
                             status=data['status'],
                             sender=self.request.user.email)

        return HttpResponseRedirect(reverse('email_functionality:dashboard'))


class UpdateMailView(LoginRequiredMixin, UpdateView):
    pass


class DeleteMailView(DeleteView):
    pass


def mail_action():
    pass


def send_mail():
    pass
