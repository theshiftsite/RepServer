from django.db import models
from django.utils import timezone

# Create your models here.
class RepCiro  (models.Model):
        StoreCode = models.CharField(max_length=10,blank=True,null=False, verbose_name='Mağaza Kodu')
        StoreDesc = models.CharField(max_length=10,blank=True,null=False, verbose_name='Mağaza Adı')
        SalesQTY = models.FloatField(verbose_name='Satış Miktarı',blank=True,null=False, default=0)
        SalesTaxBaseAmount = models.FloatField(verbose_name='VH Satış Tutarı',blank=True, null=False, default=0)
        InvoiceDate= models.DateField(default=timezone.now, verbose_name='Satış Tarihi')
        class Meta:
                verbose_name = 'Mağaza Ciro Raporu'
                verbose_name_plural = 'Mağaza Ciro Raporları'




