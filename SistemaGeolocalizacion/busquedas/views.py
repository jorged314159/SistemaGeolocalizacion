from django.shortcuts import render
from centroinvestigacion.models import CentroInvestigacion, Enfoque
from django.db.models import Q

# Create your views here.
def obtener_centros(request):
   centros = CentroInvestigacion.objects.all()
   return render(request, "buscar_centro.html", {"centros": centros})



'''
def buscar_municipio(request):
    queryset = request.GET.get("buscar")
    centros = CentroInvestigacion.objects.filter()
    if queryset:
        centros = CentroInvestigacion.objects.filter(
            Q(municipio__icontains=queryset)
        ).distinct()

    return render(request, "buscar_centro.html", {'centros': centros})

def buscar_enfoque_desc(request):
    queryset = request.GET.get("buscar")
    enfoques = Enfoque.objects.filter()
    if queryset:
        enfoques = Enfoque.objects.filter(
            Q(descripcion__icontains=queryset)
        ).distinct()
    
    return render(request, "buscar_centro.html", {'enfoques':enfoques})

def buscar_enfoque_area(request):
    queryset = request.GET.get("buscar")
    enfoques = Enfoque.objects.filter()
    if queryset:
        enfoques = Enfoque.objects.filter(
            Q(area__icontains=queryset)
        ).distinct()
    
    return render(request, "buscar_centro.html", {'enfoques':enfoques})
    
'''