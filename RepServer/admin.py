from django.contrib import admin
from .models import RepCiro
from rangefilter.filter import DateRangeFilter


# Register your models here.
@admin.register(RepCiro)
class AdminRepCiro(admin.ModelAdmin):
    list_display = ['StoreCode', 'StoreDesc', 'SalesQTY', 'SalesTaxBaseAmount']
    search_field = ['StoreCode', 'StoreDesc', 'SalesQTY', 'SalesTaxBaseAmount']
    list_filter = (
        ('InvoiceDate', DateRangeFilter), 'StoreDesc'
    )
    date_hierarchy = ['InvoiceDate']

    class Meta:
        date_hierarchy = RepCiro.InvoiceDate
