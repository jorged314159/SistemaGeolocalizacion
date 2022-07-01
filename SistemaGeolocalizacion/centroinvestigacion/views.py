from django.shortcuts import render, redirect
from django.contrib import messages
from centroinvestigacion.models import CentroInvestigacion
from centroinvestigacion.forms import FormCentroInvestigacion
from django.contrib.auth.decorators import login_required


@login_required
def lista_centros(request):
    centros = CentroInvestigacion.objects.all()
    return render(request, 'centros.html', {'centros': centros})


@login_required
def eliminar_centros(request, id):
    centro = CentroInvestigacion.objects.get(id=id)
    if request.method == 'POST':
        centro.delete()
        messages.success(request, 'Se eliminó correctamente el centro de investigación')
        return redirect('centros_lista')
    return render(request, 'eliminar_centro.html', {'centros': centro})
    


@login_required
def nuevo_centro(request):
    if request.method == 'POST':
        form = FormCentroInvestigacion(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se agregó correctamente el centro de investigación')
            return redirect('centros_lista')
    else:
        form = FormCentroInvestigacion()
    return render(request, 'nuevo_centro.html', {'form': form})


@login_required
def editar_centros(request, id):
    centro = CentroInvestigacion.objects.get(id=id)
    if request.method == 'POST':
        form = FormCentroInvestigacion(request.POST, request.FILES, instance=centro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se editó correctamente la información')
            return redirect('centros_lista')
    else:
        form = FormCentroInvestigacion(instance=centro)
    return render(request, 'editar_centro.html', {'form': form})

@login_required
def detalles_centros(request, id):
    if request.method == 'GET':
        centro = CentroInvestigacion.objects.get(id=id)
        # print(centro.nombre + centro.direccion)
        return render(request, 'detalles_centro.html', {'centros': centro})

        