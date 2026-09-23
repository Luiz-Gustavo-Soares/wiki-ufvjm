from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
    path('novo/', views.novo_evento, name='novo'),
]
