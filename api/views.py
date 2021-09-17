import json

from django.http import JsonResponse
from django.core import serializers
from .models import *


def DadosArduinoView(request, id_dados_arduino=None):
    if not id_dados_arduino:
        dados_arduino = DadosArduino.objects.all()
        if dados_arduino:
            return JsonResponse(
                json.loads(
                    serializers.serialize(
                        "json",
                        dados_arduino
                    )
                ),
                safe=False
            )
        else:
            return JsonResponse(
                {'status': 'nenhum elemento encontrado'},
                safe=False
            )
    else:
        return JsonResponse(
            json.loads(
                serializers.serialize(
                    "json",
                    DadosArduino.objects.filter(pk=id_dados_arduino)
                )
            ),
            safe=False
        )
