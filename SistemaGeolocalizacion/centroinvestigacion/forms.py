from django import forms
from centroinvestigacion.models import CentroInvestigacion, Enfoque


class FormCentroInvestigacion(forms.ModelForm):


    class Meta:
        model = CentroInvestigacion
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control'}),
            'numExterior': forms.TextInput(attrs={'class': 'form-control'}),
            'cp': forms.TextInput(attrs={'class': 'form-control'}),                                                
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control', 'readonly' : 'true'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'areaEnfoque': forms.Select(attrs={'class': 'form-select'}),
            'subAreaEnfoque': forms.Select(attrs={'class': 'form-select'}),
            'sitioWeb': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreEncargado': forms.TextInput(attrs={'class': 'form-control'}),
            'correoEncargado': forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoEncargado': forms.TextInput(attrs={'class': 'form-control'}),
        }

        imagen = forms.ImageField(widget=forms.ImageField())
        logotipo = forms.ImageField(widget=forms.ImageField())


        def __init__(self, *args, **kwargs):
            super(FormCentroInvestigacion, self).__init__(*args, **kwargs)
            self.fields['imagen'].required = False
            self.fields['logotipo'].required = False

        def clean_nombre_centro(self):
            nombre = self.cleaned_data['nombre']
            if CentroInvestigacion.object.filter(nombre = nombre).exists():
                raise forms.ValidationError('El nombre del centro o laboratorio ya se encuentra registrado.')
            return nombre

        def clean_telefono_centro(self):
            telefono = self.cleaned_data['telefono']
            if CentroInvestigacion.object.filter(telefono = telefono).exists():
                raise forms.ValidationError('El teléfono del centro o laboratorio ya se encuentra registrado.')
            return telefono

        def clean_nombreEncargado(self):
            nombreEncargado = self.cleaned_data['nombreEncargado']
            if CentroInvestigacion.object.filter(nombreEncargado = nombreEncargado).exists():
                raise forms.ValidationError('El nombre del encargado ya se encuentra registrado.')
            return nombreEncargado

class FormEnfoque(forms.ModelForm):

    class Meta:
        model = Enfoque
        fields = '__all__'

        widgets = {
            'area': forms.Select(attrs={'class': 'form-control'}),
            'subarea': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
