from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView
)

from .forms import UserCreationForm


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "authapp/register.html"
    # success_url = reverse_lazy('authapp:main')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super().form_valid(form)


class LoginView(BaseLoginView):
    template_name = 'authapp/login.html'


class LogoutView(BaseLogoutView):
    pass

