from django.db import models


GENERO_MASCULINO = "MA"
GENERO_FEMENINO = "F"
GENERO_NO_BINARIO = "X"


GENERO_CHOICES = (
        (GENERO_MASCULINO, "Masculino"),
        (GENERO_FEMENINO, "Femenino"),
        (GENERO_NO_BINARIO, "No Binario")
)


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    genero = models.CharField(choices=(GENERO_CHOICES), max_length=20)