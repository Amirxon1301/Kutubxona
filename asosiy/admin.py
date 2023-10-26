from django.contrib import admin
from django.contrib.auth.models import *

from .models import  *

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "tugilgan_yil", "jins", "tirik", "kitoblar_soni"]
    list_display_links = ["id", "ism"]
    list_editable = [ "tirik", "kitoblar_soni"]
    ordering = ["id"]
    search_fields = ["id","ism", "tugilgan_yil" ]
    search_help_text = "id ism tugilgan_yil boyicha qidiring"
    list_filter = ["jins", "tirik"]
    list_per_page = 10
    date_hierarchy = "tugilgan_yil"

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "sahifa", "janr", "muallif"]
    search_fields = ["id", "nom", "muallif__ism"]
    list_filter = ["janr"]
    ordering = ["nom"]
    autocomplete_fields = ["muallif"]

@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ["ism", "ish_vaqti"]
    search_fields = ["ism"]
    list_filter = ["ish_vaqti"]

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    search_fields = ["talaba__ism", "kitob__nom", "kutubxonachi__ism"]
# Register your models here.
# admin.site.register(Kitob)
admin.site.register(Talaba)
# admin.site.register(Muallif)
# admin.site.register(Kutubxonachi)
# admin.site.register(Record)

# admin.site.unregister(Group)
# admin.site.unregister(User)

