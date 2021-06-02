from django import forms
from django.forms import widgets
from .models import Recordatorios

class FormularioRecordatorio(forms.ModelForm):
    class Meta:
        model = Recordatorios
        fields = [
            'fechafinal',
            'asunto',
            'texto',
            'estado'
        ]
        widgets = {
            'fechafinal': forms.DateInput(attrs={
                'class': 'final form-control',
                'type': 'date',
                'placeholder': 'Tu fecha final'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'asunto form-control',
                'placeholder': 'Escribe tu asunto'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'texto form-control',
                'placeholder': 'Escribe tu texto'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class': 'estado form-control',
            })                                    
        }