# Generated by Django 5.0.3 on 2024-03-07 23:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=9)),
                ('type', models.CharField(choices=[('Goal', 'Goal'), ('Debt', 'Debt')], default=None, max_length=10)),
                ('users', models.ManyToManyField(blank=True, related_name='financial_target', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'financial_target',
            },
        ),
    ]
