# Generated by Django 2.1.2 on 2018-10-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Akreditasyon', '0008_auto_20181005_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='GameWeek',
            field=models.CharField(choices=[('1', '1'), ('3', '3'), ('4', '4'), ('2', '2')], default=0, max_length=200, verbose_name='Hafta'),
        ),
        migrations.AlterField(
            model_name='game',
            name='GameType',
            field=models.CharField(choices=[('Süper Lig', 'Süper Lig'), ('Türkiye Kupası', 'Türkiye Kupası')], default=0, max_length=200, verbose_name='Fikstür'),
        ),
    ]
