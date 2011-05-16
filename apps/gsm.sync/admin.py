from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from models import *

admin.site.register(Sport)

class ChampionshipAdmin(TranslationAdmin):
    list_display = ('gsm_id', 'sport', 'name')
    list_filter = ('sport', 'last_updated')
    search_fields = ('name_fr', 'name_en')

admin.site.register(Championship, ChampionshipAdmin)

class SeasonAdmin(TranslationAdmin):
    list_display = ('gsm_id', 'competition', 'name')
    list_filter = ('last_updated', 'competition__sport',)
    search_fields = ('competition__name_fr', 'competition__name_en', 'name_fr', 'name_en')

admin.site.register(Season, SeasonAdmin)

class CompetitionAdmin(TranslationAdmin):
    list_display = ('gsm_id', 'sport', 'area', 'championship', 'name')
    list_filter = ('sport',)
    search_fields = ('area__name_fr', 'area__name_en', 'championship__name_fr', 'championship__name_en', 'name_fr', 'name_en')

admin.site.register(Competition, CompetitionAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('gsm_id', 'name', 'area')
    search_fields = ('name', 'first_name', 'last_name')
    list_filter = ('sport', 'area')

admin.site.register(Person, PersonAdmin)

class AreaAdmin(TranslationAdmin):
    list_display = ('gsm_id', 'country_code', 'parent', 'name')
    search_fields = ('name_en', 'name_fr', 'parent__name_fr', 'parent__name_en')

admin.site.register(Area, AreaAdmin)