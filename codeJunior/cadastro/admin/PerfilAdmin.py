from django.contrib import admin

from cadastro.models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id','nome','imagem','ativo')
    search_fields = ('id','nome')