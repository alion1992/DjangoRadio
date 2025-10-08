from django.db import models
from datetime import date

# Create your models here.
class Direccion(models.Model):
    CIUDADES = [('CR','CIUDAD REAL'), ('ARG','ARGAMASILLA'), ('PUER','PUERTOLLANO'), ('AML','ALMODOVAR')]
    calle = models.CharField(max_length=10)
    numero = models.IntegerField()
    ciudad = models.CharField(choices=CIUDADES)



class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nick = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True,blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.nick} {self.id}"

    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def __str__(self):
        return f"{self.id} {self.nick}"

class Cancion(models.Model):
    nombre = models.CharField(max_length=20)
    ano_lanzamiento = models.IntegerField()
    duracion = models.IntegerField()

class Autor(models.Model):
    GENEROS = [('Pop','Pop'),('Rap','Rap'),('Reggeton','Reggeton'),('Electronica','Electronica')]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    genero = models.CharField(choices=GENEROS,max_length=12)


