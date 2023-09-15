from django.contrib import admin
from .models import Usuario, Noticia, Resena_Switch, Resena_Xbox, Resena_Play, About

admin.site.register(Usuario)
admin.site.register(Noticia)
admin.site.register(Resena_Switch)
admin.site.register(Resena_Xbox)
admin.site.register(Resena_Play)
admin.site.register(About)

