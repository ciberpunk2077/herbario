from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView

from apps.catalogo.forms.helecho import HelechoForm, HelechoUpdateForm
from apps.catalogo.models import Helecho


class HelechoListView(ListView):
    model = Helecho

    def get_queryset(self):
        return Helecho.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HelechoListView, self).get_context_data(**kwargs)
        return context


class HelechoCreateView(CreateView):
    model = Helecho
    form_class = HelechoForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(HelechoCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(HelechoCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:helecho-list')


class HelechoUpdateView(UpdateView):
    model = Helecho
    form_class = HelechoUpdateForm

    def get_context_data(self, **kwargs):
        context = super(HelechoUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(HelechoUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(HelechoUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:helecho-list')
