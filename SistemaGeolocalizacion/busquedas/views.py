from django.shortcuts import render
from centroinvestigacion.models import CentroInvestigacion, Enfoque
from django.db.models import Q

# Create your views here.
def obtener_centros(request):
   # context['api_key'] = settings.GOOGLE_MAPS_API_KEY
   centros = CentroInvestigacion.objects.all()
   return render(request, "buscar_centro.html", {"centros": centros})

def get_context_data(self, **kwargs):
   context = get_context_data(**kwargs)
   context["municipio"] = Municipio.objects.all()
   return context