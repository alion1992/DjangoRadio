from django.core.management.base import  BaseCommand
from ...models import *

class Command(BaseCommand):


    def handle(self, *args, **options):

            self.stdout.write(self.style.WARNING('Iniciando borrado de datos masivo'))
            modelos = [Reproduccion, Direccion, Cancion, Podcast, Usuario, Autor, DireccionUsuario]

            for modelo in modelos:
                modelo.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Borrado completado con exito'))
