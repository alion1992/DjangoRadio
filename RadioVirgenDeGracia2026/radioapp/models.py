
# Create your models here.
from django.db import models
from datetime import date

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nick = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    activo = models.BooleanField(default=True)


    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def __str__(self):
        return f"{self.id} {self.nick} {self.nombre} {self.apellido}"



class Direccion(models.Model):
    CIUDADES = [('CIU','CIUDAD REAL'), ('ARG','ARGAMASILLA'), ('PU','PUERTOLLANO'), ('ALM','ALMODOVAR')]
    calle = models.CharField(max_length=10)
    numero = models.IntegerField()
    ciudad = models.CharField(choices=CIUDADES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='direcciones')

    def __str__(self):
        return f"{self.id} {self.calle} {self.usuario}"


class DireccionUsuario(models.Model):
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE,related_name='usuario')
    direccion = models.ForeignKey('Direccion',on_delete=models.CASCADE,related_name='direcciones')
    preferida = models.BooleanField(default='false')
    # cuando le actualizes la direccion a un usuario que ya existe
    # que tenga una direccion a true predefinida si le metes un nueva direccion
    # preferida tienes que ponerlas todas las demas a false
    def save(self,*args,**kwargs):
        if self.preferida:
            DireccionUsuario.objects.filter(
                usuario= self.usuario
            ).exclude(
                pk=self.pk #excluimos el objeto que estamos guardando ahora mismo
            ).update(
                preferida = False #ponemos todas en false
            )
        super(DireccionUsuario,self).save(*args,**kwargs) # sin esta linea de abajo no se guarda
    def __str__(self):
        return f"{self.id} {self.usuario} {self.direccion}"

class Cancion(models.Model):


    autor = models.ForeignKey('Autor',on_delete=models.CASCADE,null=True,blank=True,related_name='canciones')
    nombre = models.CharField(max_length=20)
    ano_lanzamiento = models.IntegerField(null=True,blank=True)
    duracion = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.nombre} {self.duracion}"

class Autor(models.Model):
    GENEROS = [('P','Pop'),('R','Rap'),('RE','Reggeton'),('E','Electronica')]
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    genero = models.CharField(choices=GENEROS,max_length=12)

    def __str__(self):
        return f" {self.id} {self.nombre} {self.apellido}"

class Podcast(models.Model):
    TEMATICAS = [('T','TERROR'),('I','INVESTIGACIÓN'), ('A','ACTUALIDAD')]
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    tematica = models.CharField(choices=TEMATICAS,max_length=20)
    autores = models.ManyToManyField(Autor,related_name='podcats')

    def __str__(self):
        return f" {self.id} {self.nombre}"


class Reproduccion(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='reproducciones')
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE,null= True, blank=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE,null= True, blank=True)
    fecha_reproduccion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.id} {self.usuario} {self.cancion}"