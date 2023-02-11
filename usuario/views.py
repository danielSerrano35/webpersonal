from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import never_cache 
from django.views.decorators.csrf import csrf_protect 
from django.views.generic.edit import FormView 
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from usuario.models import Usuario
from .forms import FormularioUser, FormularioLogin
# Create your views here.

class Login(FormView):
    template_name = 'core/sesion.html'
    form_class = FormularioLogin

    success_url = reverse_lazy('cuenta')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        
        login(self.request, form.get_user()) 
        return super(Login, self).form_valid(form)
    
def logoutUsuario(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("home")
    """logout(request)
    return HttpResponseRedirect('')"""

class listado(ListView):
    model = Usuario
    template_name = 'core/cuenta.html'

    def get_queryset(self):
        return self.model.objects.filter(username=self.request.user.username)

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUser
    permission_required = ('usuario.can_open', 'usuario.can_edit', 'usuario.can_add')
    template_name = 'core/registro.html'
    success_url = reverse_lazy('cuenta')

    def post(self, request,*args, **kwargs):
        form =self.form_class(request.POST)
        if form.is_valid():
            nuevo_user = Usuario(
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos')
            )
            nuevo_user.set_password(form.cleaned_data.get('password1'))
            nuevo_user.save()
            return redirect('cuenta')
        else:
            form.errors
            return render(request, self.template_name,{'form':form})