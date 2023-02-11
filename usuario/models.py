from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Manejo(BaseUserManager):
    def createuser(self, email, username, nombres, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo!')
        usuario = self.model(
            username=username, 
            email = self.normalize_email(email), 
            nombres =nombres
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, username, email, nombres, password):
        usuario = self.createuser(
            email, 
            username=username, 
            nombres =nombres,
            password=password
        )
        usuario.admin = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', max_length=100, null=True, unique=True)
    edad = models.IntegerField('edad',null=True, blank=True)
    email = models.EmailField('Correo Electrónico', unique=True)
    nombres = models.CharField( max_length=100, null=True, blank=True)
    apellidos = models.CharField( max_length=100, null=True, blank=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200,null=True, blank=True)
    activo = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    objects = Manejo()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self, perm, obj= None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.admin