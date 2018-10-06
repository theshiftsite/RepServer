from django.utils import timezone
from django.db import models


# Create your models here.
class Game(models.Model):
    GAMETYPE_CHOICES = {

        ('Süper Lig', 'Süper Lig'),
        ('Türkiye Kupası', 'Türkiye Kupası'),

    }

    GAMEWEEK_CHOICES = {
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')
    }
    ID = models.AutoField
    GameCode = models.CharField(max_length=10, blank=True, null=False, verbose_name='Maç Kodu')
    GameHome = models.CharField(max_length=50, blank=True, null=False, verbose_name='Ev Sahibi Takım')
    GameAway = models.CharField(max_length=50, blank=True, null=False, verbose_name='Misafir Takım')
    GameDate = models.DateTimeField(default=timezone.now, verbose_name='Maç Tarihi')
    GameWeek = models.CharField(choices=GAMEWEEK_CHOICES, max_length=200, default=0, verbose_name='Hafta')
    GameRef = models.CharField(max_length=100, blank=True, null=False, verbose_name='Maç Hakemi')
    GameType = models.CharField(choices=GAMETYPE_CHOICES, max_length=200, default=0, verbose_name='Fikstür')

    class Meta:
        verbose_name = 'Maç'
        verbose_name_plural = 'Maçlar'

    def publsih(self):
        self.save()

    def __str__(self):
        return self.GameCode


class Organization(models.Model):
    OrgCode = models.BigIntegerField(blank=True, null=False, verbose_name='Kurum Kodu', editable=True)
    OrgName = models.CharField(max_length=100, blank=True, null=False, verbose_name='Kurum Adı')
    eMail = models.EmailField(verbose_name='E-Posta', blank=True, null=False)
    Phone = models.CharField(max_length=100, blank=True, null=False, verbose_name='Telefon')
    Country = models.CharField(max_length=100, blank=True, null=False, verbose_name='Ülke')
    City = models.CharField(max_length=100, blank=True, null=False, verbose_name='Şehir/Eyalet')
    District = models.CharField(max_length=100, blank=True, null=False, verbose_name='İlçe')
    AddressDetail = models.CharField(max_length=100, blank=True, null=False, verbose_name='Adres')

    class Meta:
        verbose_name = 'Kurum'
        verbose_name_plural = 'Kurumlar'

class OrgAcreditation(models.Model):
    AcredidatedGuestName = models.CharField(max_length=100, blank=True, null=False, verbose_name='Misafir Adı')
    AcredidatedLastName = models.CharField(max_length=100, blank=True, null=False, verbose_name='Misafir SoyAdı')
    AcredidatedGuestIdentity = models.CharField(max_length=100, blank=True, null=False, verbose_name='Tc Kimlik No',
                                            primary_key=True)
    AcredidatedEmail = models.EmailField
    AcredidatedMobilePhone = models.CharField(max_length=10, blank=True, null=False)
    AcrGameCode = models.ForeignKey(Game, on_delete=models.CASCADE)
    AcrGameDate = models.OneToOneField(to='Akreditasyon.OrgAcreditation',on_delete=models.CASCADE,related_name='GameDate')

    class Meta:
        verbose_name = 'Misafir'
        verbose_name_plural = 'Misafirler'


