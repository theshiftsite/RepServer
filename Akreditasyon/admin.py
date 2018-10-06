from django.contrib import admin
from .models import Organization, Game

# Register your models here.

#@admin.register(OrgAcreditation)
#class AdminOrgAcreditaion(admin.ModelAdmin):
 #   list_display = ('AcredidatedGuestName', 'AcredidatedLastName','AcredidatedGuestIdentity','AcrGameCode')
  #  list_per_page = 20
   # list_filter =  ('AcredidatedGuestName', 'AcredidatedLastName','AcredidatedGuestIdentity','AcrGameCode')






@admin.register(Organization)
class AdminOrganization(admin.ModelAdmin):
    list_display = ['OrgCode', 'OrgName', 'eMail', 'Phone', 'District', 'City']
    search_fields = ['OrgCode', 'OrgName', 'eMail', 'Phone', 'District', 'City']
    list_filter = ['OrgCode', 'OrgName', 'eMail', 'Phone', 'District', 'City']
    list_per_page = 20


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    list_display = ('GameCode', 'GameHome', 'GameAway', 'GameType', 'GameRef')
    list_display_links = ('GameHome','GameAway')
    list_filter = ('GameCode', 'GameHome', 'GameAway', 'GameRef')
    search_fields = ('GameCode', 'GameHome', 'GameAway')
