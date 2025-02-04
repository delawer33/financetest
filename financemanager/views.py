from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from rest_framework import permissions, viewsets, filters
from rest_framework.response import Response

from .forms import TransactionCreateForm
from .models import Transaction, Category
from .serializers import TransactionSerializer


@login_required
def dashboard(request):
    return render(request, 'financemanager/dashboard.html')


def get_categories_by_type(request):
    transaction_type = request.GET.get('type')
    categories = Category.objects.filter(type=transaction_type)
    return render(
        request,
        'financemanager/category_dropdown.html',
        {'categories': categories}
    )


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


class TransactionViewset(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user).order_by('-id')

    class Meta:
        ordering = ['-id']
