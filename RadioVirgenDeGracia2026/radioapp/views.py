import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Cancion
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
'''
def listar_canciones(request):
    canciones = Cancion.objects.all().values("id", "nombre")
    return JsonResponse(list(canciones), safe=False)

def detalle_cancion(request, id):
    try:
        cancion = Cancion.objects.values("id", "nombre").get(id=id)
        return JsonResponse(cancion)
    except Cancion.DoesNotExist:
        return JsonResponse({"error": "Canción no encontrada"}, status=404)

@csrf_exempt
def borrar_cancion(request, id):
    if request.method == 'DELETE':
        try:

            cancion = Cancion.objects.get(pk=id)
            cancion.delete()

            return JsonResponse({'mensaje': 'Cancion eliminado correctamente'})
        except Cancion.DoesNotExist as e:
            return JsonResponse({"error": "Error al borrar la cancion" + e.message}, status=404)
    return JsonResponse({'error': 'No permitido'})


@csrf_exempt
def crear_cancion(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cancion = Cancion.objects.create(**data)
        return JsonResponse({'mensaje': 'Canción creada', 'id': cancion.id})

    return JsonResponse({'error': 'Operación incorrecta'})+

'''
@csrf_exempt
def get_cancion(request,id):
    if request.method == "GET":
        try:
            cancion = Cancion.objects.values().get(id=id)
            return JsonResponse(cancion)
        except Cancion.DoesNotExist:
            return JsonResponse({"error": "Canción no encontrada"}, status=404)
    else:
        return JsonResponse({"error": "Operación no soportada"})
@csrf_exempt
def add_cancion(request):
    if request.method  == 'POST':
        jsonCancion = json.loads(request.body)
        cancion = Cancion.objects.create(**jsonCancion)
        return JsonResponse({"cancion": "Se insertado correctamente"})
    else:
        return JsonResponse({"error": "Operación no soportada"})

def get_canciones(request):
    canciones = Cancion.objects.all().values()
    return JsonResponse(list(canciones),safe=False)

