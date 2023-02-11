from django.contrib import admin
from .models import Autos, Categoria, Venta
# Register your models here.
admin.site.register(Autos)
admin.site.register(Categoria)
admin.site.register(Venta)