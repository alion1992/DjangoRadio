from django.core.management.base import BaseCommand
from faker import Faker
from ...models import *

import random

fake = Faker('es_ES')


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando script de carga masiva'))
        if any([Usuario.objects.exists(), Cancion.objects.exists(), Direccion.objects.exists(),
                Podcast.objects.exists(), Reproduccion.objects.exists()]):
            self.stdout.write(self.style.ERROR('Error, ya existen datos en la base de datos'))
            return
        self.stdout.write(self.style.SUCCESS('La base de datos esta vacia, procedemos a cargar los datos'))
        # como las canciones como los podcats tienen autores vamos a crear unos pocos primeros, 15 por ejemplo, buen numero
        self.stdout.write('Creando 15 autores')
        autores = []
        generos = [g[0] for g in Autor.GENEROS]
        for g in range(15):
            autor = Autor.objects.create(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                genero=random.choice(generos)
            )
            autores.append(autor)
        self.stdout.write(self.style.SUCCESS('15 autores creados'))
        # creamos 20 usuarios y 2 direcciones para cada uno
        self.stdout.write('creando 20 usuarios y 2 direcciones para cada uno')
        usuarios = []
        ciudades_disponibles = [c[0] for c in Direccion.CIUDADES]
        for u in range(20):
            usuario = Usuario.objects.create(
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                nick=fake.user_name(),
                fecha_nacimiento=fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90),
                telefono=fake.phone_number(),
                email=fake.email(),
            )
        usuarios.append(usuario)
        # creamos 2 direcciones para cada usuario
        for i in range(2):
            Direccion.objects.create(
                usuario=usuario,
                calle=fake.street_name(),
                numero=fake.building_number(),
                ciudad=random.choice(ciudades_disponibles)

            )
        self.stdout.write(self.style.SUCCESS('USuarios y direcciones creados con exito'))


        self.stdout.write('Creando 30 canciones')
        canciones = [];
        for i in range(30):
            cancion = Cancion.objects.create(
                nombre=fake.catch_phrase(),
                duracion=random.randint(60, 400),
                autor=random.choice(autores),
                ano_lanzamiento=random.randint(1950, 2023)
            )
            canciones.append(cancion)


        self.stdout.write('Creando 50 podcats')
        podcasts = []
        tematicas_disponibles = [t[0] for t in Podcast.TEMATICAS]
        for i in range(50):
            podcast = Podcast.objects.create(
                nombre=fake.sentence(nb_words=6),
                descripcion=fake.text(max_nb_chars=200),
                tematica=random.choice(tematicas_disponibles),
            )
            autores_podcast = random.sample(autores, k=random.randint(1, 4))
            podcast.autores.set(autores_podcast)
            podcasts.append(podcast)
        self.stdout.write(self.style.SUCCESS('podcast creados con exito'))

        self.stdout.write('Creando 500 reproducciones')
        for i in range(500):
            usuario_reproduccion = random.choice(usuarios)

            if random.choice([True, False]):
                # es cancion
                cancion_reproducida = random.choice(canciones)
                ano_lanzamiento = random.randint(1950, 2023)
                Reproduccion.objects.create(
                    usuario=usuario_reproduccion,
                    cancion=cancion_reproducida,
                )
            else:
                podcast_reproducido = random.choice(podcasts)
                Reproduccion.objects.create(
                    usuario=usuario_reproduccion,
                    podcast=podcast_reproducido,
                )
        self.stdout.write(self.style.SUCCESS('Cargado'))