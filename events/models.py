from django.db import models
from django.contrib.auth.models import User
from wiki.models import Pagina 

class Evento(models.Model):
    titulo = models.CharField(max_length=200, help_text="Nome do evento (ex: Semana da Computação)")
    descricao = models.TextField(blank=True, null=True, help_text="Detalhes sobre o evento")
    
    data_hora_evento = models.DateTimeField(help_text="Data e hora em que o evento ocorrerá")
    
    organizador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='eventos_organizados')
    
    local = models.ForeignKey(Pagina, on_delete=models.SET_NULL, null=True, related_name='eventos_no_local', help_text="Página da wiki correspondente ao local do evento")
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} ({self.data_hora_evento.strftime('%d/%m/%Y %H:%M')})"
