from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CreditosForm, ClientesForm
from .models import Creditos, Clientes
import random
# Create your views here.

"""
Funciones para la gestion de creditos
"""


def creditos_list(request):
    context = {'creditos_list': Creditos.objects.all()}
    return render(request, "creditos/creditos_lists.html", context)


def creditos_form(request, id=0):
    total = 0
    decision = ""
    ranking = 0
    if(request.method == "GET"):
        if(id == 0):
            form = CreditosForm()
        else:  # Modo de editar el cliente
            creditos = Creditos.objects.get(pk=id)
            data_clientes = Creditos.objects.filter(pk=id).values('nombre_id')
            data = Creditos.objects.all().values('monto', 'nombre')
            # Recorrer los montos que ha solicitado el cliente
            for i in data:
                for j in data_clientes:
                    if(j['nombre_id'] == i['nombre']):
                        total = total + i['monto']
            print(total)

            if(total > 50000):
                ranking = random.randint(0, 7)
                decision = "No es recomendable aplicarlo, se puede endeudar mas"
            else:
                ranking = random.randint(5, 10)
                decision = "Si se puede aplicar, es un cliente sin deudas :D"
            form = CreditosForm(instance=creditos)
        return render(request, "creditos/creditos_form.html", {'form': form, 'total': total, 'decision': decision, 'ranking': ranking})
    else:
        if(id == 0):
            form = CreditosForm(request.POST)
        else:  # Cuando insertas el cliente
            creditos = Creditos.objects.get(pk=id)
            form = CreditosForm(request.POST, instance=creditos)
        if(form.is_valid()):
            form.save()
        return redirect('/creditos/')


def creditos_eliminar(request, id):
    creditos = Creditos.objects.get(pk=id)
    creditos.delete()
    return redirect('/creditos/')


"""
Funciones para la gestion del cliente
"""


def clientes_list(request):
    context = {'clientes_list': Clientes.objects.all()}
    return render(request, "clientes/clientes_lists.html", context)


def clientes_form(request, id=0):
    if(request.method == "GET"):
        if(id == 0):
            form = ClientesForm()
        else:
            clientes = Clientes.objects.get(pk=id)
            form = ClientesForm(instance=clientes)
        return render(request, "clientes/clientes_form.html", {'form': form})
    else:
        if(id == 0):
            form = ClientesForm(request.POST)
        else:
            clientes = Clientes.objects.get(pk=id)
            form = ClientesForm(request.POST, instance=clientes)
        if(form.is_valid()):
            form.save()
        return redirect('/creditos/cliente/')


def clientes_delete(request, id):
    clientes = Clientes.objects.get(pk=id)
    clientes.delete()
    return redirect('/creditos/cliente/')
