# Generated by Django 2.1.2 on 2018-10-05 00:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RepServer', '0007_auto_20181005_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='repciro',
            name='InvoiceDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
