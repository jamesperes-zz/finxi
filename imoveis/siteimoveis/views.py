from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import geocoder

from .forms import ImovelForm, VendedorForm
from .models import Imovel, Vendedor


def imovelhome(request):
    imoveis_localizados = Imovel.objects.all()
    imoveis = Imovel.objects.order_by('?')[:3]
    ip = get_client_ip(request)
    local = geocoder.ip('177.192.118.248')
    if local.lat == None or local.lng == None:
        lat = '-22.9710987'
        lng = '-43.1868393'

    lat = str(local.lat)
    lng = str(local.lng)
    return render(request, 'siteimoveis/home.html', {'imoveis': imoveis_localizados,
                                                     'lat':lat,
                                                     'lng':lng,
                                                     'imoveis3': imoveis})

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

def imovelpesquisa(request):
    mapas = Imovel.objects.all()
    search = request.POST.get('pesquisa')
    pesquisas = Imovel.objects.filter(bairro=search.lower())
    ip = get_client_ip(request)
    local = geocoder.ip('177.192.118.248')
    if local.lat == None or local.lng == None:
        lat = '-22.9710987'
        lng = '-43.1868393'

    lat = str(local.lat)
    lng = str(local.lng)
    return render(request, 'siteimoveis/pesquisa.html', {'pesquisas':pesquisas,
                                                         'lat':lat,
                                                         'lng':lng,
                                                         'mapas':mapas})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def imovel_list(request):
    imoveis = Imovel.objects.all().order_by('bairro')
    return render(request, 'siteimoveis/list.html', {'imoveis': imoveis})

def imovel(request, imovel_id):
    imovel = Imovel.objects.get(id=imovel_id)
    return render(request, 'siteimoveis/imovel.html', {'imovel': imovel})
