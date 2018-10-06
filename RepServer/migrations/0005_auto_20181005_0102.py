# Generated by Django 2.1.2 on 2018-10-04 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RepServer', '0004_auto_20181005_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repciro',
            options={'verbose_name': 'Mağaza Ciro Raporu', 'verbose_name_plural': 'Mağaza Ciro Raporları'},
        ),
        migrations.AddField(
            model_name='repciro',
            name='EndDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='repciro',
            name='SalesInvoiceDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='repciro',
            name='StartDate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]