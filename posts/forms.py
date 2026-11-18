
from django import forms
from .models import Post


# Formulario para crear y editar publicaciones
class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'titulo',
            'contenido',
            'autor',
            'estado',
            'imagen'
        ]
