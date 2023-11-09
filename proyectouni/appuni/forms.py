from django import forms
from .models import Alumno, MATERIAS

class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        labels = {
            'nombre': 'Nombre y Apellido',
            'edad': 'Edad',
            'materia': 'Materia',
        }

    materia = forms.ChoiceField(
        choices=MATERIAS, 
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
