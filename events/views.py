from django.shortcuts import render
from events.forms import EventoForm


def novo_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            local = form.cleaned_data['local']
            data = form.cleaned_data['data']
            print(nome, local, data)

    else:
        form = EventoForm()

    context = {'form': form}
    return render(request, 'events/novo_evento.html', context)
