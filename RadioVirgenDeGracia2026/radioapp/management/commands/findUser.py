from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random


class Command(BaseCommand):


    def handle(self, *args, **options):
        try:
            if Usuario.objects.exists():
                usuarios = Usuario.objects.filter(nombre__icontains='a',activo=False)
                print(len(usuarios))
                if len(usuarios) == 0:
                    raise Exception("No hemos encontrado ningun usuario")
                for usuario in usuarios:
                    print(usuario.nombre)
            else:
                raise Exception("No hay usuarios")

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error {e}'))