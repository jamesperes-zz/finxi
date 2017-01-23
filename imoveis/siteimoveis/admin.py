from django.contrib import admin
from .models import Vendedor, Imovel

#class VendedorAdmin(admin.ModelAdmin):
#    pass


#class ImovelAdmin(admin.ModelAdmin):
#    pass


class ImovelAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag','endereco', 'valor', 'bairro', 'anuncio', 'vendedor', 'cidade', 'latitude', 'longitude')
    list_display = ('image_tag', 'endereco', 'valor', 'bairro', 'anuncio',  'vendedor')
    #def __str__(self):
    #    return self.anuncio

admin.site.register(Imovel, ImovelAdmin)
