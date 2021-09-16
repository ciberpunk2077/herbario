from django import forms

from apps.catalogo.extra import ESTADOS
from .base import BaseForm
from apps.catalogo.models import Algas


class AlgasForm(BaseForm):
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    class Meta:
        model = Algas
        fields = ('nombre_cientifico', 'nombre_comun','especie',  'genero','fecha', 'numero_recolecta', 'municipio', 'colonia', 'descripcion','nombre_colector','imagen')
        widgets = {
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'})
        }


class AlgasUpdateForm(BaseForm):
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    class Meta:
        model = Algas
        fields = ('nombre_cientifico', 'nombre_comun','especie','genero','fecha', 'numero_recolecta', 'municipio', 'colonia', 'descripcion','nombre_colector','imagen')