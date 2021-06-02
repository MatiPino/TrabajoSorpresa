from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Recordatorios
from .forms import FormularioRecordatorio

def index(request):

    formularioR = FormularioRecordatorio()
    if request.method == 'POST':
        formularioR = FormularioRecordatorio(request.POST)
        if formularioR.is_valid():
            formularioR.save()   
    context = {'formulario': formularioR}
    
    return render(request, 'recordatorios.html', context)




