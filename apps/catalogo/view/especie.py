from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView

from apps.catalogo.forms.especie import especieForm, especieUpdateForm
from apps.catalogo.models import especie


class especieListView(ListView):
    model = especie

    def get_queryset(self):
        return especie.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(especieListView, self).get_context_data(**kwargs)
        return context


class especieCreateView(CreateView):
    model = especie
    form_class = especieForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(especieCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(especieCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:alga-list')


class especieUpdateView(UpdateView):
    model = especie
    form_class = especieUpdateForm

    def get_context_data(self, **kwargs):
        context = super(especieUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(especieUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(especieUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:especie-list')
