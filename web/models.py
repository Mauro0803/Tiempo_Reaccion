from django.db import models

# Create your models here.
class Prueba(models.Model):                     
    prueba_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 64)
    letra_1 = models.CharField(max_length= 1)
    tiempo_1 = models.FloatField(default=0.0,)
    letra_2 = models.CharField(max_length= 1)
    tiempo_2 = models.FloatField(default=0.0)
    letra_3 = models.CharField(max_length= 1)
    tiempo_3 = models.FloatField(default=0.0)
    letra_4 = models.CharField(max_length= 1)
    tiempo_4 = models.FloatField(default=0.0)
    letra_5 = models.CharField(max_length= 1)
    tiempo_5 = models.FloatField(default=0.0)

    def calcular_promedio(self):
        tiempos = [self.tiempo_1, self.tiempo_2, self.tiempo_3, self.tiempo_4, self.tiempo_5]
        tiempos_validos = [t for t in tiempos if t > 0] 
        if tiempos_validos:
            return sum(tiempos_validos) / len(tiempos_validos)
        return 0.0


