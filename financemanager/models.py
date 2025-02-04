from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Type(models.TextChoices):
    INCOME = "INCOME", "Income"
    OUTCOME = "OUTCOME", "Outcome"


class Category(models.Model):
    name = models.CharField(
        'Name',
        max_length=50
    )

    type = models.CharField(
        "Type",
        max_length=20,
        choices=Type.choices,
        default=Type.OUTCOME
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

    type = models.CharField(
        "Type",
        max_length=20,
        choices=Type.choices,
        default=Type.OUTCOME
    )

    amount = models.DecimalField(
        max_digits=16,
        decimal_places=2
    )

    date = models.DateField(
        default=timezone.now
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

    def clean(self):
        if self.category and self.category.type != self.type:
            raise ValidationError(
                f"Category '{self.category.name}' does not match Transaction "
                f"type '{self.type}'"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
