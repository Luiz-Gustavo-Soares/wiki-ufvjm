from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from wiki.models import Pagina
from wiki.forms import PaginaForm



def wiki_busca_view(request):
    query = request.GET.get('q', '')

    if query:
        paginas = Pagina.objects.filter(titulo__icontains=query).order_by('-atualizado_em')

    else: 
        paginas = Pagina.objects.all().order_by('-atualizado_em')

    
    context = {
        'paginas': paginas,
        'query': query
    }        

    return render(request, 'wiki/busca_resultados.html', context=context)



def pagina_detalhe_view(request, pagina_slug):
    pagina = get_object_or_404(Pagina, slug=pagina_slug) # Pagina.objects.get(slug=pagina_slug)

    context = {
        'pagina': pagina
    }

    return render(request, 'wiki/pagina_detalhe.html', context=context)


@login_required
def pagina_criar_view(request):

    if request.method == 'POST':
        form = PaginaForm(request.POST)
        if form.is_valid():
            nova_pagina = form.save(commit=False)
            nova_pagina.autor = request.user
            nova_pagina.save()
            form.save_m2m()

            return redirect('wiki:detalhe', pagina_slug=nova_pagina.slug)

    else:
        form = PaginaForm()

    context = {
        'form': form
    }
    return render(request, 'wiki/pagina_form.html', context=context)



@login_required
def pagina_edit_view(request, pagina_slug):
    pagina = get_object_or_404(Pagina, slug=pagina_slug)    

    if request.method == 'POST':
        form = PaginaForm(request.POST, instance=pagina)
        
        if form.is_valid():
            nova_pagina = form.save(commit=False)
            nova_pagina.autor = request.user
            nova_pagina.save()
            form.save_m2m()
            
            return redirect('wiki:detalhe', pagina_slug=nova_pagina.slug)
    else:
        form = PaginaForm(instance=pagina)
        
    context = {
        'form': form,
        'edit': True
    }
    return render(request, 'wiki/pagina_form.html', context=context)
