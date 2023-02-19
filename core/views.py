from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from Inventario.models import Autos
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# Create your views here.
def home(request):
    
    autos = Autos.objects.all()
    return render(request, "core\home.html", {"autos":autos})
@csrf_exempt
def datos(request):
    input_text = request.POST.get('my_input', None)
    autos1 = Autos.objects.all()
    context = {'autos1':autos1, 'input_text':input_text}
    return render(request, "core\datos.html", context)

def registro(request):
    return render(request, "core/registro.html")

def compra(request):
    return render(request, "core/compra.html")

def about(request):
    return render(request, "core/about.html")

def cuenta(request):
    return render(request, "core/cuenta.html")


class autos_vista(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Autos.objects.all()
        context[data] = data
        return context
