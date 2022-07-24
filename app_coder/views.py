from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Familiar
def familia(request, nombre, edad, cumpleanos):
    familia = Familiar(nombre=nombre, edad=edad, cumpleanos=cumpleanos)
    familia.save()
    return HttpResponse(f"""
        <p>{familia.nombre} - {familia.edad} - {familia.cumpleanos}""")
def lista_familia(request):
    lista= Familiar.objects.all()
    return render(request, "template1.html", {"listafamilia": lista})
# Create your views here.
