from django import forms


from .base import BaseForm
from apps.catalogo.models import Especie


class EspecieForm(BaseForm):


    class Meta:
        model = Especie
        fields = ('nombre', 'familia','descripcion')


class EspecieUpdateForm(BaseForm):

    class Meta:
        model = Especie
        fields = ('nombre', 'familia','descripcion')