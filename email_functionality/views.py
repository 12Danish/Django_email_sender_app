from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import WriteMailForm
from .models import Mails
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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
        mail_instance = Mails.objects.create(user=self.request.user,
                                             subject=data['subject'],
                                             recipient=data['recipient'],
                                             body=data['body'],
                                             status=data['status'],
                                             sender=self.request.user.email)

        # Calling django's built in send_mail function to send the mail to the email address provided
        try:
            send_email(mail_instance)
        except Exception as e:
            return HttpResponseRedirect(reverse('email_functionality:dashboard'),
                                        {'error': e}
                                        )
        # Redirecting to the dashboard view
        return HttpResponseRedirect(reverse('email_functionality:dashboard'))


# This view handles the update functionality
class UpdateMailView(LoginRequiredMixin, UpdateView):
    model = Mails  # Referring to the model class
    form_class = WriteMailForm  # referring to the form class
    template_name = 'email_functionality/update_mail.html'  # name of the template to display
    success_url = reverse_lazy('email_functionality:dashboard')  # url to redirect

    def form_valid(self, form):
        # Getting the updated subject
        updated_subject = form.cleaned_data['subject']
        # getting the updated body
        updated_body = form.cleaned_data['body']

        # Getting the existing mail
        mail_instance = self.get_object()
        mail_instance.subject = f'{updated_subject} (edited)'
        mail_instance.body = updated_body

        # Saving the changes within my database
        mail_instance.save()

        # Sending the updated mail to the recipient
        send_email(mail_instance)
        # Returning this so that the default behaviour of updating also takes place
        return super().form_valid(form)


@login_required
def delete_mail(request, pk):
    if request.method == 'POST':
        # Filter the mail instance based on the logged-in user
        mail_instance = get_object_or_404(Mails, id=pk, user=request.user)

        # Deleting the selected mail
        mail_instance.delete()

        # Returning a JSON response with a success message
        return JsonResponse(
            {'message': 'The mail was deleted successfully', 'redirect_url': reverse('email_functionality:dashboard')})
    else:
        # Returning a JSON response with the error
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def send_email(mail_instance):
    send_mail(subject=mail_instance.subject,
              message=mail_instance.body,
              from_email=mail_instance.sender,
              recipient_list=[mail_instance.recipient],
              fail_silently=False  # Set this to True if you want to suppress email sending errors
              )
