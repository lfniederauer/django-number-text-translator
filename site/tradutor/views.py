# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views import View
from . import tradutor

class TradutorView(View):
    def get(self, request, *args, **kwargs):
        numero = self.kwargs.get("numero")
        sinal = self.kwargs.get("sinal")
        sinal_msg = ""
        if sinal == "-":
            sinal_msg = "menos"
        ext = tradutor.dExtenso()
        result = {}
        if int(numero) > 99999 or int(numero) < -99999:
            result['erro'] = 'Os números podem estar no intervalo [-99999, 99999].'
            result['bônus'] = sinal_msg + ext.getExtenso(str(numero))
        else:
            result['extenso'] = sinal_msg + ext.getExtenso(str(numero))
        return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii':False})