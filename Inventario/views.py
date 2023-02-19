from django.shortcuts import render, redirect
from .models import Autos, Venta
from  django.views.decorators.csrf import csrf_protect
from .forms import FormVenta
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    autos = Autos.objects.all()
    return render(request, "home.html", {"autos": autos})

def datos(request):
    autoss = Autos.objects.all()
    return render(request, "datos.html", {"autos": autoss})


"""class Venta(LoginRequiredMixin,CreateView): 
    model=Venta
    form_class = form_venta
    template_name = 'core/compra.html' 
    
    def post(self, request, ):
        form = self.form_class(request.POST)
        if form.is_valid():
        # <process form cleaned data>
            return redirect('home')"""
@csrf_protect
def agregarVenta(request):
    input_text = request.POST.get('my_input1', None)
    if request.method == 'POST':
        Form = FormVenta(request.POST, request.FILES)
        if Form.is_valid():
            Form.auto_id = input_text
            Form.save()
            return redirect('home')
    else:
        Form = FormVenta()
    return render(request, 'compra.html',
                  {'Form': Form})
