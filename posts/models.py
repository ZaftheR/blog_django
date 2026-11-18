from django.db import models


# Modelo para representar una publicación del blog
class Post(models.Model):

    ESTADOS = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='borrador'
    )
    
    # Imagen opcional de la publicación
    imagen = models.ImageField(
    upload_to='posts/',
    null=True,
    blank=True
    )
    
    
    def __str__(self):
        return self.titulo






