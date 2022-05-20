from django import forms
from centroinvestigacion.models import CentroInvestigacion, Enfoque

class FormCentroInvestigacion(forms.ModelForm):

    class Meta:
        model = CentroInvestigacion
        fields = '__all__'
        
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Calle, #No, Colonia, C.P, Municipio'}),
            'latitud' : forms.TextInput(attrs={'class' : 'form-control'}),
            'longitud' : forms.TextInput(attrs={'class' : 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class' : 'form-control'}),
            'enfoque' : forms.Select(attrs={'class' : 'form-control'}),
            
        }
        
        
class FormEnfoque(forms.ModelForm):
    
    class Meta:
        model = Enfoque
        fields = '__all__'
        
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control'}),
            
        }