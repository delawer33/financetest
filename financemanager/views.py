from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .forms import TransactionCreateForm
from .models import Transaction


@login_required
def dashboard(request):
    return render(request, 'financemanager/dashboard.html')


class TransactionCreate(LoginRequiredMixin, CreateView):
    form_class = TransactionCreateForm
    template_name = 'financemanager/createtransaction.html'
    success_url = reverse_lazy('finance:dashboard')

    def form_valid(self, form):
        trans = form.save(commit=False)
        trans.user = self.request.user
        return super().form_valid(form)


class History(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'financemanager/history.html'
    context_object_name = 'transactions'

    # def get_queryset(self):
