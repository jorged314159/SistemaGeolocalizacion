from django.shortcuts import render
from django.conf import settings

from centroinvestigacion.models import CentroInvestigacion, Municipio
from centroinvestigacion.forms import FormCentroInvestigacion

# Create your views here.
def obtener_centros(request):
   # context['api_key'] = settings.GOOGLE_MAPS_API_KEY
   centros = CentroInvestigacion.objects.all()
   return render(request, "buscar_centro.html", {"centros": centros, 'api_key':settings.GOOGLE_MAPS_API_KEY})

def get_context_data(self, **kwargs):
   context = get_context_data(**kwargs)
   context["municipio"] = Municipio.objects.all()
   return context