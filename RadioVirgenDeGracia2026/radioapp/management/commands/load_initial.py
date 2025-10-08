from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *
import random


class Command(BaseCommand):


    def handle(self, *args, **options):
        try:
            fake = Faker('es_ES')
            self.stdout.write(self.style.SUCCESS('INICIAMOS LA CARGA DE LOS DATOS'))

            self.stdout.write(self.style.SUCCESS('Carga de usuarios'))

            for i in range(30):
                Usuario.objects.create(nombre=fake.first_name(),apellido=fake.last_name(),nick=fake.user_name(),fecha_nacimiento=fake.date_of_birth(minimum_age=18,maximum_age=18),telefono=fake.phone_number(),email=fake.email())
                self.stdout.write(self.style.SUCCESS(f'Se ha insertertado {i} Persona'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'ERROR {e}'))
