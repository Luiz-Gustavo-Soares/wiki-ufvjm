from django.contrib import admin
from unfold.admin import ModelAdmin
from wiki.models import Pagina, Categoria, Tag


@admin.register(Pagina)
class PaginaAdmin(ModelAdmin):
    list_display = ['titulo', 'categoria', 'autor', 'ativo', 'atualizado_em',]

    readonly_fields = ['criado_em', 'atualizado_em']

    list_filter = ['categoria', 'criado_em']

    search_fields = ['titulo']


    @admin.action(description='Desativar')
    def desativar_paginas(modeladmin, request, queryset):
        queryset.update(ativo=False)

    actions = [desativar_paginas,]


@admin.register(Categoria)
class CategoriaAdmin(ModelAdmin):
    pass

admin.site.register(Tag)
