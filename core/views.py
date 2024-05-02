from django.shortcuts import render
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    usuarios = request.user
    evento = Evento.objects.filter(usuarios=usuarios)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
