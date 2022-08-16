from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages


class SignUpView(CreateView):
    """
    a view to create a new user
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_success_url(self):
        """
        override the function to add a message after success SignUp
        """
        messages.success(self.request, _('Account successfully Created!'))
        return super().get_success_url()
