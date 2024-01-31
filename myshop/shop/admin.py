from django.contrib import admin
from .models import Kategoria, Produkt

# Register your models here.

@admin.register(Kategoria )
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'slug']
    prepopulated_fields = {'slug': ('nazwa',)}

@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'slug', 'cena',
                    'dostepne', 'created', 'updated']
    list_filter = ['dostepne', 'created', 'updated']
    list_editable = ['cena', 'dostepne']
    prepopulated_fields = {'slug': ('nazwa',)}
