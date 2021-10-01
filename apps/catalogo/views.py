from msilib.schema import ListView

from django.db.models import Q
from django.shortcuts import render

# Create your view here.
from django.views.generic import TemplateView

from apps.catalogo.models import Planta, Especie, FrutoSemilla, Familia, Algas, Polen, Helecho, Hongo


class HomeViews(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeViews, self).get_context_data(**kwargs)
        search=self.request.GET.get('search')
        if search:
            planta=Planta.objects.filter(Q(nombre_comun__icontains=search) | Q(nombre_cientifico__icontains=search))
            frutosemilla=FrutoSemilla.objects.filter(Q(nombre_comun__icontains=search) | Q(nombre_cientifico__icontains=search))
            algas=Algas.objects.filter(Q(nombre_comun__icontains=search) | Q(nombre_cientifico__icontains=search))
            polen = Polen.objects.filter(Q(nombre_comun__icontains=search) | Q(nombre_cientifico__icontains=search))
            helecho = Helecho.objects.filter(Q(nombre_comun__icontains=search) | Q(nombre_cientifico__icontains=search))
            hongo = Hongo.objects.filter(Q(nombre_comun__icontains=search) | Q(nombre_cientifico__icontains=search))
            especie=Especie.objects.filter(Q(nombre__icontains=search) | Q(descripcion__icontains=search))
            familia=Familia.objects.filter(Q(nombre__icontains=search) | Q(descripcion__icontains=search))
            context['search']=True
            context['especies']=especie
            context['plantas']=planta
            context['alga']=algas
            context['polens'] = polen
            context['frutosemillas']=frutosemilla
            context['familias']=familia
            context['helechos']=helecho
            context['hongos']=hongo
        return context


class PresentacionView(TemplateView):
    template_name = '../templates/presentacion.html'

    def get_context_data(self, **kwargs):
        context = super(PresentacionView, self).get_context_data(**kwargs)
        return context

class ColeccionView(TemplateView):
    template_name = '../templates/coleccion.html'

    def get_context_data(self, **kwargs):
        context = super(ColeccionView, self).get_context_data(**kwargs)
        return context

class InvestigacionView(TemplateView):
    template_name = '../templates/investigacion.html'

    def get_context_data(self, **kwargs):
        context = super(InvestigacionView, self).get_context_data(**kwargs)
        return context

class PersonalView(TemplateView):
    template_name = '../templates/personal.html'

    def get_context_data(self, **kwargs):
        context = super(PersonalView, self).get_context_data(**kwargs)
        return context
