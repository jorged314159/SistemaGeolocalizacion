from django.shortcuts import render
from busquedas.models import Busqueda

# Create your views here.
def buscar_centro(request):
    busqueda = Busqueda()
    return render(request, 'inicio.html', {'busquedas': busqueda})
    