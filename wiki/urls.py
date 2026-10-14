from django.urls import path
from wiki import views

app_name = 'wiki'

urlpatterns = [
    path('criar/', views.pagina_criar_view, name='criar_pagina'),
    path('busca/', views.wiki_busca_view, name='busca'),
    path('edit/<slug:pagina_slug>/', views.pagina_edit_view, name='editar'),
    
    path('<slug:pagina_slug>/', views.pagina_detalhe_view, name='detalhe'),
    
]
