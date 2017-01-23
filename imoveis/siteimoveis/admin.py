from django.contrib import admin
from .models import Vendedor, Imovel


class ImovelAdmin(admin.ModelAdmin):

    readonly_fields = ('image_tag','endereco', 'valor', 'bairro', 'anuncio', 'vendedor', 'cidade', 'latitude', 'longitude')

    list_display = ('image_tag', 'endereco', 'valor', 'bairro', 'anuncio',  'vendedor')

admin.site.register(Imovel, ImovelAdmin)
