from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView

from apps.catalogo.forms.alga import AlgasForm, AlgasUpdateForm
from apps.catalogo.models import Algas


class AlgasListView(ListView):
    model = Algas

    def get_queryset(self):
        return Algas.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AlgasListView, self).get_context_data(**kwargs)
        return context


class AlgasCreateView(CreateView):
    model = Algas
    form_class = AlgasForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(AlgasCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(AlgasCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:alga-list')


class AlgasUpdateView(UpdateView):
    model = Algas
    form_class = AlgasUpdateForm

    def get_context_data(self, **kwargs):
        context = super(AlgasUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(AlgasUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(AlgasUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:alga-list')
