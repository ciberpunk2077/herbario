from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView

from apps.catalogo.forms.planta import PlantaForm, PlantaUpdateForm
from apps.catalogo.models import Planta


class PlantaListView(ListView):
    model = Planta

    def get_queryset(self):
        return Planta.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PlantaListView, self).get_context_data(**kwargs)
        return context


class PlantaCreateView(CreateView):
    model = Planta
    form_class = PlantaForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(PlantaCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(PlantaCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:planta-list')


class PlantaUpdateView(UpdateView):
    model = Planta
    form_class = PlantaUpdateForm

    def get_context_data(self, **kwargs):
        context = super(PlantaUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(PlantaUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(PlantaUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:planta-list')

class PlantaDetailView(TemplateView):
    template_name = 'catalogo/planta_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlantaDetailView, self).get_context_data(**kwargs)
        pk_planta = self.kwargs.get('pk')
        context['planta'] = Planta.objects.get(pk=pk_planta)
        return context

class PlantaDeleteView(DeleteView):
    model = Planta

    def get_success_url(self):
        messages.success(self.request, "El registro ha sido eliminado con éxito.")
        return reverse_lazy('catalogo:planta-list')