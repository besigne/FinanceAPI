from django.db import models
from .User import User


class Transaction(models.Model):
    class TypeEnum(models.TextChoices):
        INCOME = 'Income'
        SPENT = 'Spent'
        INVESTMENT = 'Investment'
        DEBT = 'Debt'

    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null=True)
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
        db_table = "transaction"
