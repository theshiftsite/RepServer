# Generated by Django 2.1.2 on 2018-10-05 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Akreditasyon', '0006_game_gametype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='GameAway',
            field=models.CharField(blank=True, max_length=50, verbose_name='Misafir Takım'),
        ),
        migrations.AlterField(
            model_name='game',
            name='GameCode',
            field=models.CharField(blank=True, max_length=10, verbose_name='Maç Kodu'),
        ),
        migrations.AlterField(
            model_name='game',
            name='GameDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Maç Tarihi'),
        ),
        migrations.AlterField(
            model_name='game',
            name='GameHome',
            field=models.CharField(blank=True, max_length=50, verbose_name='Ev Sahibi Takım'),
        ),
        migrations.AlterField(
            model_name='game',
            name='GameRef',
            field=models.CharField(blank=True, max_length=10, verbose_name='Maç Hakemi'),
        ),
        migrations.AlterField(
            model_name='game',
            name='GameType',
            field=models.CharField(choices=[('Süper Lig', 'Süper Lig'), ('Türkiye Kupası', 'Türkiye Kupası')], default=0, max_length=200, verbose_name='Fikstür'),
        ),
    ]
