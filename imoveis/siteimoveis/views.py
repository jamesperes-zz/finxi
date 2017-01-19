from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ImovelForm, VendedorForm
from .models import Imovel, Vendedor


def imovelhome(request):
    imoveis_localizados = Imovel.objects.all()
    return render(request, 'siteimoveis/home.html', {'imoveis': imoveis_localizados})


def imovel_novo(request):
    if request.method == "POST":
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ImovelForm()
    return render(request, 'siteimoveis/imovel_novo.html', {'form': form})

def vendedor_novo(request):
    if request.method == "POST":
        form = VendedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = VendedorForm()
    return render(request, 'siteimoveis/vendedor_novo.html', {'form': form})
