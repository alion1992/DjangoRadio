from django.contrib import admin
from .models  import *
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cancion)
admin.site.register(Autor)
admin.site.register(Reproduccion)
admin.site.register(Podcast)
admin.site.register(DireccionUsuario)