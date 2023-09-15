from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    nombre_usuario = models.CharField(
        max_length=255, unique=True, verbose_name='Nombre de usuario')
    email = models.EmailField(verbose_name='Correo electrónico')
    contrasena = models.CharField(max_length=255, verbose_name='Contraseña')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    direccion_despacho = models.TextField(
        max_length=255, blank=True, null=True, verbose_name='Dirección de despacho')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'core_usuario'

    def __str__(self):
        return self.nombre_usuario
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    video_embed = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
    
class Resena_Switch(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='post_images')
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
    
class Resena_Xbox(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='post_images')
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
    
class Resena_Play(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='post_images')
    contenido = models.TextField()

    def __str__(self):
        return self.titulo
    
class About(models.Model):
    titulo = models.CharField(max_length=200)
    about = models.TextField()
    editor = models.TextField()

    def __str__(self):
        return self.titulo