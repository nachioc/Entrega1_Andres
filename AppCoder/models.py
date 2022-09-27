from django.db import models




class Familiar(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class Profesion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'


class Mascota(models.Model):
    nombre = models.CharField(max_length=128)
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.edad}'
