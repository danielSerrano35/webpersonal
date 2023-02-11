from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import RegistrarUsuario, listado
urlpatterns = [
    path('cuenta/',login_required(listado.as_view()), name="cuenta"),
    path('registro/',login_required(RegistrarUsuario.as_view()), name="registro"),
]