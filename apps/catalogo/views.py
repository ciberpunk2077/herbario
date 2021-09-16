from msilib.schema import ListView

from django.shortcuts import render

# Create your view here.
from django.views.generic import TemplateView


class HomeViews(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeViews, self).get_context_data(**kwargs)
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
