from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView

from apps.catalogo.forms.polen import PolenForm, PolenUpdateForm
from apps.catalogo.models import Polen


class PolenListView(ListView):
    model = Polen

    def get_queryset(self):
        return Polen.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PolenListView, self).get_context_data(**kwargs)
        return context


class PolenCreateView(CreateView):
    model = Polen
    form_class = PolenForm

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.save()
        messages.success(self.request, "El registro ha sido creadao con éxito.")
        return super(PolenCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(PolenCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:polen-list')


class PolenUpdateView(UpdateView):
    model = Polen
    form_class = PolenUpdateForm

    def get_context_data(self, **kwargs):
        context = super(PolenUpdateView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        form.instance.user_by = self.request.user.pk
        form.instance.updated_at = now()
        form.save()
        messages.success(self.request, "El registro ha sido actualizado con éxito.")
        return super(PolenUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(PolenUpdateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('catalogo:polen-list')

class PolenDetailView(TemplateView):
    template_name = 'catalogo/polen_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PolenDetailView, self).get_context_data(**kwargs)
        pk_polen = self.kwargs.get('pk')
        context['polen'] = Polen.objects.get(pk=pk_polen)
        return context

class PolenDeleteView(DeleteView):
    model = Polen

    def get_success_url(self):
        messages.success(self.request, "El registro ha sido eliminado con éxito.")
        return reverse_lazy('catalogo:polen-list')
