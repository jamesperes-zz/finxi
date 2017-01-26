from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db.models import Q

import geocoder
from geopy.distance import vincenty


from .forms import ImovelForm, VendedorForm
from .models import Imovel


api_google = settings.GOOGLE_API_KEY


def imovel_home(request):
    imoveis_localizados = Imovel.objects.all()
    imoveis = imoveis_localizados.order_by('?')[:3]
    # não esta usando pq django pega o ip do servidor
    ip = get_client_ip(request)
    # colocar a variavel ip aqui
    local = geocoder.ip('177.192.118.248')
    if local.lat is None or local.lng is None:
        lat = '-22.9710987'
        lng = '-43.1868393'

    lat = str(local.lat)
    lng = str(local.lng)
    api = api_google
    return render(request,
                  'siteimoveis/home.html', {'imoveis': imoveis_localizados,
                                            'lat': lat, 'lng': lng,
                                            'imoveis3': imoveis,
                                            'api': api})


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


def imovel_pesquisa(request):
    mapas = Imovel.objects.all()
    search = request.POST.get('pesquisa')
    pesquisas = mapas.filter(
        Q(bairro__icontains=search) | Q(endereco__icontains=search)
    )

    ip = get_client_ip(request)
    local = geocoder.ip('177.192.118.248')
    if not local.lat or not local.lng:
        lat = '-22.9710987'
        lng = '-43.1868393'

    lat = str(local.lat)
    lng = str(local.lng)
    api = api_google
    return render(request, 'siteimoveis/pesquisa.html',
                  {'pesquisas': pesquisas,
                   'lat': lat,
                   'lng': lng,
                   'mapas': mapas,
                   'api': api})


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


def imovel_proximos(request):
 #   import ipdb; ipdb.set_trace()
    imoveis = Imovel.objects.all()
    search = request.POST.get('pesquisa')
    endereco_pesquisado = geocoder.google(search)
    lat_pesquisada = str(endereco_pesquisado.lat)
    lng_pesquisada = str(endereco_pesquisado.lng)
    ponto = (lat_pesquisada, lng_pesquisada)
    encontrados = []
    for imovel in imoveis:
        if vincenty(ponto, (imovel.latitude,
                            imovel.longitude)).kilometers <= 1.0:
            encontrados.append(imovel)
            print(imovel)

    return render(request, 'siteimoveis/pesquisapro.html',
                  {'imoveis': imoveis,
                   'encontrados': encontrados})
