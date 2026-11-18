from django.contrib import admin
from .models import Perfil


# Configuración del perfil en el administrador
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = ('user', 'link_web')
    search_fields = ('user__username',)
