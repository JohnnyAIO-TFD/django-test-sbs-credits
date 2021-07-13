from django import forms
from .models import Clientes, Creditos


class CreditosForm(forms.ModelForm):
    class Meta:
        model = Creditos
        fields = ('nombre', 'monto', 'aprobado')
        labels = {
            'nombre': 'Nombre Completo',
            'monto': 'Monto a Solicitar en USD',
            'aprobado': 'Estado de aprobacion'
        }

    def __init__(self, *args, **kwargs):
        super(CreditosForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].empty_label = "Select"
        self.fields['aprobado'].required = False


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('nombre', 'dni')
        labels = {
            'nombre': 'Nombre Completo',
            'dni': 'Numero de Identidad'
        }
