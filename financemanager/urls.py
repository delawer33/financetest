from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    dashboard,
    TransactionCreate,
    History,
    TransactionViewset,
    get_categories_by_type,
)


app_name = 'finance'

router = DefaultRouter()
router.register('transactions', TransactionViewset)

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', TransactionCreate.as_view(), name='create-trans'),
    path('history/', History.as_view(), name='history'),
    path('get_categories/', get_categories_by_type, name='get-categories'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
