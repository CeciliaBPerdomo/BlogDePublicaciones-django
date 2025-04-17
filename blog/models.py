from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Estado(models.TextChoices):
        PUBLICADO = 'P', 'Publicado'
        BORRADOR = 'B', 'Borrador'
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    estado = models.CharField(
        max_length=1,
        choices=Estado.choices,
        default=Estado.BORRADOR,
    )
 
    def __str__(self):
        return self.titulo
    

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"