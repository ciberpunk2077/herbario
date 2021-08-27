from django import forms


from .base import BaseForm
from apps.catalogo.models import genero


class generoForm(BaseForm):


    class Meta:
        model = genero
        fields = ('nombre', 'descripcion')


class generoUpdateForm(BaseForm):

    class Meta:
        model = genero
        fields = ('nombre','descripcion')