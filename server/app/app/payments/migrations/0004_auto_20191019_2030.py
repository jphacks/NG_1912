# Generated by Django 2.2.5 on 2019-10-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_payment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='tax_rate',
            field=models.PositiveSmallIntegerField(blank=True, default=8),
        ),
    ]
