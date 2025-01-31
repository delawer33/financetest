from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(
        'Name',
        max_length=50
    )

    def __str__(self):
        return self.name


class Transaction(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    type = models.BooleanField(
        'Type (checked - income, not checked - outcome)',
        default=True
    )

    amount = models.DecimalField(
        max_digits=16,
        decimal_places=2
    )

    date = models.DateField(
        auto_now_add=True
    )

    description = models.TextField(
        max_length=255,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
