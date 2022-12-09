from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    PROFESOR = 'P'
    ALUMNO = 'A'
    TYPE_USER = [
        (PROFESOR, 'Profesor'),
        (ALUMNO, 'Alumno')
    ]

    username = None
    email = models.EmailField('email', unique=True)
    tipo = models.CharField('tipo', max_length=1, choices=TYPE_USER)
    foto = models.CharField('foto', max_length=500, default="https://pbs.twimg.com/profile_images/2258320866/540101_381698941864058_100000718650124_1190836_894968735_n_400x400.jpg")
    telefono = models.IntegerField('telefono', default=1000000)
    carrera = models.CharField('Carrera', max_length=35, default="Ingenieria Informatica")
    perfil = models.CharField('perfil', max_length=500, default='Sin perfil')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.tipo == 'P':
            return f'Profesor {self.first_name} {self.last_name}'
        return f'Alumno {self.first_name} {self.last_name}'
        


class Asignatura(models.Model):
    seccion = models.CharField('seccion', max_length=7, null=False)
    nombre_asignatura = models.CharField(
        'nombre_asignatura', max_length=50, null=False)
    profesor = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'tipo': 'P'})

    def __str__(self):
        return f'{self.nombre_asignatura} seccion {self.seccion} del profesor {self.profesor}'

class Asistencia(models.Model):
    fecha_clase = models.DateField('fecha_clase', auto_now_add=True)
    alumno = models.ForeignKey(
        User, on_delete=models.CASCADE,  limit_choices_to={'tipo': 'A'})
    asignatura = models.ForeignKey(
        Asignatura, on_delete=models.CASCADE, )