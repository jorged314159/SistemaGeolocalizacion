from django.shortcuts import render, redirect
from centroinvestigacion.models import CentroInvestigacion
from centroinvestigacion.forms import FormCentroInvestigacion
from django.contrib.auth.decorators import login_required

@login_required
def lista_centros(request):
    centros = CentroInvestigacion.objects.all()
    return render(request, 'centros.html', {'centros': centros})

@login_required
def eliminar_centros(request, id):
    CentroInvestigacion.objects.get(id = id).delete()
    return redirect('centros_lista')

@login_required
def nuevo_centro(request):
    if request.method == 'POST':
        form = FormCentroInvestigacion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centros_lista')
    else:
        form = FormCentroInvestigacion()
    return render(request, 'nuevo_centro.html', {'form': form})

@login_required
def editar_centros(request, id):
    centro = CentroInvestigacion.objects.get(id = id)
    if request.method == 'POST':
        form = FormCentroInvestigacion(request.POST, instance=centro)
        if form.is_valid():
            form.save()
            return redirect('centros_lista')
    else:
        form = FormCentroInvestigacion(instance=centro)
    return render(request, 'editar_centro.html', {'form': form})