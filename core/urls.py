from django.urls import path

from core.views import home, sobre

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre),
]
