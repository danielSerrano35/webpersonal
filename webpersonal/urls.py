"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from core import views
from Inventario import views as vv
from usuario import views as v

app_name = "core"

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/',v.RegistrarUsuario.as_view(), name="registro"),
    path('compra/', vv.agregarVenta, name='compra'),
    path('login/',v.Login.as_view(),name ='login'),
    path('logout/',v.logoutUsuario,name ='logout'),
    path('datos/', views.datos, name="datos"),
    path('about/', views.about, name="about"),
    path('cuenta/', v.listado.as_view(), name="cuenta"),
    path('actualizar_usuario/', v.UpdateUserView.as_view(), name="editar_usuario"),
    path('delete_user/<int:pk>/', v.DeleteUser.as_view(), name="eliminar_usuario"),
    path('admin/', admin.site.urls),
]
