from django.contrib import admin

# Register your models here.
from apps.catalogo.models import *

@admin.register(Algas)
class algasAdmin(admin.ModelAdmin):
    list_display = ('nombre_cientifico','numero_recolecta')

# Register your models here.
admin.site.register(Familia)
admin.site.register(Especie)
admin.site.register(Municipio)
admin.site.register(Planta)
admin.site.register(FrutoSemilla)
admin.site.register(Polen)
admin.site.register(Helecho)
admin.site.register(Hongo)
