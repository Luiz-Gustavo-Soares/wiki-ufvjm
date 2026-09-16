from django.urls import path

from core.views import home, sobre


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
]
