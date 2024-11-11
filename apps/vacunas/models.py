from django.db import models

# Create your models here.
# Vacuna:
# - Nombre
# - Codigo
# - Nombre tecnico *
# - Cantidad de Dosis


# Dosis:
# - es de una vacuna -> referencia a la vacuna -> ForeignKey
# - nombre de la dosis
# - orden



class Vacuna(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)
    ca_dosis = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'vacunas'
        verbose_name = u'vacuna'
        verbose_name_plural = u'vacunas'
        
    def __str__(self):
        return self.nombre



class Dosis(models.Model):
    vacuna = models.ForeignKey(Vacuna, related_name='dosis_de_vacuna', on_delete=models.CASCADE, null=True)
    orden = models.IntegerField()
    nombre = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'dosis'
        verbose_name = u'dosis'
        verbose_name_plural = u'dosis'
        
    def __str__(self):
        return self.nombre