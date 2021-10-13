import folium
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView

from apps.catalogo.forms.frutosemilla import FrutoSemillaForm, FrutoSemillaUpdateForm
from apps.catalogo.models import FrutoSemilla


class FrutoSemillaListView(ListView):
    model = FrutoSemilla

    def get_queryset(self):
        return FrutoSemilla.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FrutoSemillaListView, self).get_context_data(**kwargs)
        return context


class FrutoSemillaCreateView(CreateView):
    model = FrutoSemilla
    form_class = FrutoSemillaForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(FrutoSemillaCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(FrutoSemillaCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:frutosemilla-list')


class FrutoSemillaUpdateView(UpdateView):
    model = FrutoSemilla
    form_class = FrutoSemillaUpdateForm

    def get_context_data(self, **kwargs):
        context = super(FrutoSemillaUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(FrutoSemillaUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(FrutoSemillaUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:frutosemilla-list')

class FrutoSemillaDetailView(TemplateView):
    template_name = 'catalogo/frutosemilla_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FrutoSemillaDetailView, self).get_context_data(**kwargs)
        pk_frutosemilla = self.kwargs.get('pk')
        context['frutosemilla'] = FrutoSemilla.objects.get(pk=pk_frutosemilla)
        return context

class FrutoSemillaDeleteView(DeleteView):
    model = FrutoSemilla

    def get_success_url(self):
        messages.success(self.request, "El registro ha sido eliminado con éxito.")
        return reverse_lazy('catalogo:frutosemilla-list')
