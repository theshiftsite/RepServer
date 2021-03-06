# Generated by Django 2.1.2 on 2018-10-05 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Akreditasyon', '0003_auto_20181005_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GameCode', models.CharField(blank=True, max_length=10)),
                ('GameHome', models.CharField(blank=True, max_length=50)),
                ('GameAway', models.CharField(blank=True, max_length=50)),
                ('GameDate', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Maç',
                'verbose_name_plural': 'Maçlar',
            },
        ),
    ]
