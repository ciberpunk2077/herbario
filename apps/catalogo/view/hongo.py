from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView, TemplateView

from apps.catalogo.forms.hongo import HongoForm, HongoUpdateForm
from apps.catalogo.models import Hongo


class HongoListView(ListView):
    model = Hongo

    def get_queryset(self):
        return Hongo.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HongoListView, self).get_context_data(**kwargs)
        return context


class HongoCreateView(CreateView):
    model = Hongo
    form_class = HongoForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(HongoCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(HongoCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:hongo-list')


class HongoUpdateView(UpdateView):
    model = Hongo
    form_class = HongoUpdateForm

    def get_context_data(self, **kwargs):
        context = super(HongoUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(HongoUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(HongoUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:hongo-list')

class HongoDetailView(TemplateView):
    template_name = 'catalogo/hongo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(HongoDetailView, self).get_context_data(**kwargs)
        pk_hongo = self.kwargs.get('pk')
        context['hongo'] = Hongo.objects.get(pk=pk_hongo)
        return context
