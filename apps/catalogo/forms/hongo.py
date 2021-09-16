from django import forms

from apps.catalogo.extra import ESTADOS
from .base import BaseForm
from apps.catalogo.models import Hongo


class HongoForm(BaseForm):
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    class Meta:
        model = Hongo
        fields = ('nombre_cientifico', 'nombre_comun','especie',  'genero','fecha', 'numero_recolecta', 'municipio', 'colonia', 'descripcion','nombre_colector','imagen')
        widgets = {
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'})
        }


class HongoUpdateForm(BaseForm):
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    class Meta:
        model = Hongo
        fields = ('nombre_cientifico', 'nombre_comun','especie','genero','fecha', 'numero_recolecta', 'municipio', 'colonia', 'descripcion','nombre_colector','imagen')