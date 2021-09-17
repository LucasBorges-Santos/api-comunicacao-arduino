from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('dados-arduinos/<int:id_dados_arduino>/', views.DadosArduinoView, name="dados-arduinos"),
    path('dados-arduinos/', views.DadosArduinoView, name="dados-arduinos")
]