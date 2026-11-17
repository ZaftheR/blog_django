from django.contrib import admin
from .models import Post


# Configuración del panel administrativo
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'estado', 'fecha_creacion')
    list_filter = ('estado',)
    search_fields = ('titulo', 'autor')


# Registrar el modelo Post en el administrador
admin.site.register(Post, PostAdmin)

