from django.shortcuts import render, redirect
from django.contrib import messages
from centroinvestigacion.models import Area, Enfoque, CentroInvestigacion
from centroinvestigacion.forms import FormCentroInvestigacion
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect






class ListaCentros(LoginRequiredMixin, ListView):
    model = CentroInvestigacion

class NuevoCentro(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = CentroInvestigacion
    form_class = FormCentroInvestigacion
    success_url = reverse_lazy('centros_lista')
    extra_context = {'accion': 'Nuevo'}
    success_message = "Se agregó el centro de investigación correctamente"

    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(NuevoCentro, self).get_context_data(**kwargs)
        context["areaEnfoque"] = Area.objects.all()
        context["subAreaEnfoque"] = Enfoque.objects.all()
        return context
    


class EditarCentro(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = CentroInvestigacion
    form_class = FormCentroInvestigacion
    success_url = reverse_lazy('centros_lista')
    extra_context = {'accion' : 'Editar'}
    success_message = "Se editó la información correctamente"

    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(EditarCentro, self).get_context_data(**kwargs)
        context["areaEnfoque"] = Area.objects.all()
        context["subAreaEnfoque"] = Enfoque.objects.all()
        context["obj"] = CentroInvestigacion.objects.filter(pk=pk).first()
        return context



class EliminarCentro(LoginRequiredMixin, DeleteView):
    model = CentroInvestigacion
    success_url = reverse_lazy('centros_lista')

    def form_valid(self, form):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Se eliminó con éxito')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

@login_required
def detalles_centros(request, id):
    if request.method == 'GET':
        centro = CentroInvestigacion.objects.get(id=id)
        # print(centro.nombre + centro.direccion)
        return render(request, 'detalles_centro.html', {'centros': centro})

# @login_required
# def lista_centros(request):
#     centros = CentroInvestigacion.objects.all()
#     return render(request, 'centros.html', {'centros': centros})


# @login_required
# def eliminar_centros(request, id):
#     centro = CentroInvestigacion.objects.get(id=id)
#     if request.method == 'POST':
#         centro.delete()
#         messages.success(request, 'Se eliminó correctamente el centro de investigación')
#         return redirect('centros_lista')
#     return render(request, 'eliminar_centro.html', {'centros': centro})
    


# @login_required
# def nuevo_centro(request):
#     if request.method == 'POST':
#         form = FormCentroInvestigacion(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Se agregó correctamente el centro de investigación')
#             return redirect('centros_lista')
#     else:
#         form = FormCentroInvestigacion()
#     return render(request, 'nuevo_centro.html', {'form': form})


# @login_required
# def editar_centros(request, id):
#     centro = CentroInvestigacion.objects.get(id=id)
#     if request.method == 'POST':
#         form = FormCentroInvestigacion(request.POST, request.FILES, instance=centro)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Se editó correctamente la información')
#             return redirect('centros_lista')
#     else:
#         form = FormCentroInvestigacion(instance=centro)
#     return render(request, 'editar_centro.html', {'form': form})



     