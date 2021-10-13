from django import forms

from apps.catalogo.extra import ESTADOS
from .base import BaseForm
from apps.catalogo.models import Polen


class PolenForm(BaseForm):
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    class Meta:
        model = Polen
        fields = ('nombre_cientifico', 'nombre_comun','especie',  'genero','fecha', 'numero_recolecta', 'municipio', 'colonia', 'descripcion','nombre_colector','imagen','latitud','longitud')
        widgets = {
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'})
        }


class PolenUpdateForm(BaseForm):
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    class Meta:
        model = Polen
        fields = ('nombre_cientifico', 'nombre_comun','especie','genero','fecha', 'numero_recolecta', 'municipio', 'colonia', 'descripcion','nombre_colector','imagen','latitud','longitud')