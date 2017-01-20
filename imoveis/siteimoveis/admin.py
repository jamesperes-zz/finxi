from django.contrib import admin
from .models import Vendedor, Imovel

#class VendedorAdmin(admin.ModelAdmin):
#    pass


#class ImovelAdmin(admin.ModelAdmin):
#    pass


class ImovelAdmin(admin.ModelAdmin):
    readonly_fields = ('endereco', 'valor', 'bairro', 'anuncio', 'imagem', 'vendedor')
    list_display = ('endereco', 'valor', 'bairro', 'anuncio', 'imagem', 'vendedor')
    #def __str__(self):
    #    return self.anuncio

admin.site.register(Imovel, ImovelAdmin)
