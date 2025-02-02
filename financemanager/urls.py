from django.urls import path

from .views import (
    dashboard,
    TransactionCreate,
    History
)


app_name = 'finance'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', TransactionCreate.as_view(), name='create-trans'),
    path('history/', History.as_view(), name='history'),
]
