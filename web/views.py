from django.shortcuts import render
from django.http import JsonResponse
from web.models import Prueba
import json
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def resultados(request):
    pruebas = Prueba.objects.all()
    datos_combinados = []
    for prueba in pruebas:
        promedio = round(prueba.calcular_promedio(), 4)
        datos_combinados.append({
            'nombre': prueba.nombre,
            'letra_1': prueba.letra_1,
            'tiempo_1': prueba.tiempo_1,
            'letra_2': prueba.letra_2,
            'tiempo_2': prueba.tiempo_2,
            'letra_3': prueba.letra_3,
            'tiempo_3': prueba.tiempo_3,
            'letra_4': prueba.letra_4,
            'tiempo_4': prueba.tiempo_4,
            'letra_5': prueba.letra_5,
            'tiempo_5': prueba.tiempo_5,
            'promedio': promedio,
        })

    return render(request, 'resultados.html', {'datos_combinados': datos_combinados})

def submit_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        responses = data.get('responses')

        prueba = Prueba(nombre=nombre)

        if len(responses) >= 5:
            prueba.letra_1 = responses[0]['letter']
            prueba.tiempo_1 = responses[0]['time']
            prueba.letra_2 = responses[1]['letter']
            prueba.tiempo_2 = responses[1]['time']
            prueba.letra_3 = responses[2]['letter']
            prueba.tiempo_3 = responses[2]['time']
            prueba.letra_4 = responses[3]['letter']
            prueba.tiempo_4 = responses[3]['time']
            prueba.letra_5 = responses[4]['letter']
            prueba.tiempo_5 = responses[4]['time']

            prueba.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)