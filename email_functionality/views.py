from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import WriteMailForm
from .models import Mails
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse


# This view handles the dashboard view
class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'email_functionality/dashboard.html'  # Referring to the Html template
    context_object_name = 'emails'  # this is the name of the query set

    def get_queryset(self):
        user = self.request.user  # setting user variable to the logged in user
        return Mails.objects.filter(user=user)  # returning the mails related to the user


# This function displays the mails saved as drafts
class DraftsView(LoginRequiredMixin, ListView):
    template_name = 'email_functionality/drafts_view.html'  # Referring to Html templates
    context_object_name = 'emails'  # This is the query set name

    def get_queryset(self):  # Getting the query set with this function
        user = self.request.user  # specifying the user to the currently logged in user
        return Mails.objects.filter(user=user, status='draft')  # Returning users drafts


# This function displays the mails and details
class MailDetailsView(LoginRequiredMixin, DetailView):
    model = Mails  # Specifying model
    template_name = 'email_functionality/mail_details.html'  # Referring to Html template
    context_object_name = 'mail'  # Specifying the query set name


# This function displays form to write mail
class WriteMail(LoginRequiredMixin, FormView):
    template_name = 'email_functionality/write_mail.html'  # Referring to Html template
    form_class = WriteMailForm  # Defining the class of forms. This has been imported from the forms file

    def form_valid(self, form):  # Handles form_validation
        data = form.cleaned_data  # Getting form data
        # Creating and instance of the model
        Mails.objects.create(user=self.request.user,
                             subject=data['subject'],
                             recipient=data['recipient'],
                             body=data['body'],
                             status=data['status'],
                             sender=self.request.user.email)

        return HttpResponseRedirect(reverse('email_functionality:dashboard'))


class UpdateMailView(LoginRequiredMixin, UpdateView):
    pass


class DeleteMailView(LoginRequiredMixin, DeleteView):
    model = Mails
    success_url = reverse_lazy('email_functionality:dashboard')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse('Object deleted successfully', status=200)


def mail_action():
    pass


def send_mail():
    pass
