from django.urls import path
from inicio.views import inicio, sobre_mi

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre_mi', sobre_mi, name='sobre_mi')
]