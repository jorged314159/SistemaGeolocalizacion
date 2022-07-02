from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from centroinvestigacion.models import Enfoque, CentroInvestigacion
from centroinvestigacion.forms import FormEnfoque


class PaginaInicio(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ListaEnfoques(LoginRequiredMixin, ListView):
    model = Enfoque


class NuevoEnfoqueView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Enfoque
    # fields = '__all__'
    form_class = FormEnfoque
    success_url = reverse_lazy('enfoques_lista')
    extra_context = {'accion': 'Nuevo'}
    success_message = "Se agregó el enfoque de manera exitosa"


class EditarEnfoqueView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Enfoque
    # fields = '__all__'
    form_class = FormEnfoque
    success_url = reverse_lazy('enfoques_lista')
    extra_context = {'accion': 'Editar'}
    success_message = "Se editó la información de manera exitosa"


class EliminarEnfoqueView(LoginRequiredMixin, DeleteView):
    model = Enfoque
    success_url = reverse_lazy('enfoques_lista')

    def form_valid(self, form):
        self.object = self.get_object()
        if CentroInvestigacion.objects.filter(enfoque=self.object):
            messages.error(
                self.request, 'No se puede eliminar el enfoque, ' +
                'tiene centros de investigacion agregados')
            pass
        else:
            self.object.delete()
            messages.success(self.request, 'Se eliminó con éxito')

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)
