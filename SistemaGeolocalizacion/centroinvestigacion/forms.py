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
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'cp': forms.TextInput(attrs={'class': 'form-control'}),                                                
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control', 'readonly' : 'true'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'areaEnfoque': forms.Select(attrs={'class': 'form-control'}),
            'subAreaEnfoque': forms.Select(attrs={'class': 'form-control'}),
            'sitioWeb': forms.TextInput(attrs={'class': 'form-control'}),
        }
        imagen = forms.ImageField(widget=forms.ImageField())
        


class FormEnfoque(forms.ModelForm):

    class Meta:
        model = Enfoque
        fields = '__all__'

        widgets = {
            'area': forms.Select(attrs={'class': 'form-control'}),
            'subArea': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
