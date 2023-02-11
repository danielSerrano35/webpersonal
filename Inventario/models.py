from django.db import models
from usuario.models import Usuario
from autoslug import AutoSlugField


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=250, default='SOME STRING')
    slug = AutoSlugField(populate_from='nombre', default='SOME STRING')
    activo = models.BooleanField(default=True)

    def __str__(self) ->str:
        return self.nombre

    class Meta:
        verbose_name_plural: 'Categoria'

class Autos(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    modelo = models.CharField(max_length=250, default='SOME STRING')
    slug = AutoSlugField(populate_from='nombre', default='SOME STRING')
    imagen = models.CharField(max_length=250, default='SOME STRING')
    marca = models.CharField(max_length=20, default='SOME STRING')
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self) ->str:
        return self.modelo
    
    class Meta:
        db_table= 'autos'
        verbose_name_plural= 'Autos'



class Venta(models.Model):
    num = models.AutoField(primary_key=True)
    id_auto = models.ForeignKey(Autos, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, max_length=250, default='SOME STRING')
    fecha = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) ->str:
        return str(self.id_auto)
    

    class Meta:
        verbose_name_plural: 'Venta'

        
