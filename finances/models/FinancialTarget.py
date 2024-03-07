from django.db import models
from .User import User


class FinancialTarget(models.Model):
    class TypeEnum(models.Choices):
        GOAL = 'Goal'
        DEBT = 'Debt'

    users = models.ManyToManyField(User, related_name='financial_target', blank=True)
    value = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )
    type = models.CharField(
        max_length=10,
        choices=TypeEnum.choices,
        default=None
    )

    class Meta:
        db_table = "financial_target"
