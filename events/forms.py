from django import forms

class EventoForm(forms.Form):
    nome = forms.CharField(
        label='Nome do evento',
        max_length=100,
    )

    local = forms.CharField(
        label="Local",
        max_length=100
    )

    data = forms.DateField(
        label='Data do Evento',
        widget=forms.DateInput(attrs={"type": "date"})
    )
