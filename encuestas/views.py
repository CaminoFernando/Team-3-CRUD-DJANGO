from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gretting(request):
    return HttpResponse("Hello world from Django for Codo a Codo 4.0")

def saludo(request):
    return HttpResponse("Saludos! desde django para codo a codo")    


def datos(request):
    return HttpResponse("Por favor complete sus datos personales")
