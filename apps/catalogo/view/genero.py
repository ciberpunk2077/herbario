from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView

from apps.catalogo.forms.genero import generoForm, generoUpdateForm
from apps.catalogo.models import genero


class generoListView(ListView):
    model = genero

    def get_queryset(self):
        return genero.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(generoListView, self).get_context_data(**kwargs)
        return context


class generoCreateView(CreateView):
    model = genero
    form_class = generoForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(generoCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(generoCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:genero-list')


class generoUpdateView(UpdateView):
    model = genero
    form_class = generoUpdateForm

    def get_context_data(self, **kwargs):
        context = super(generoUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(generoUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(generoUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:genero-list')
