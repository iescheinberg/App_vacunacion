from django.shortcuts import render, redirect
from .forms import FormPaciente

from .models import Paciente
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# Create your views here.


""" def lista(request):
    return render(request, 'pacientes/lista.html', {}) """

class Lista(ListView):
    template_name = 'pacientes/lista.html'
    model = Paciente
    context_object_name = 'pacientes'
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        ctx = super(Lista, self).get_context_data(**kwargs)
        ctx['titulo'] = 'Lista de Pacientes🤒'
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all().order_by('apellido')




class Nuevo(CreateView):
    template_name = 'pacientes/nuevo.html'
    model = Paciente
    form_class = FormPaciente
    success_url = reverse_lazy('pacientes:lista')

    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        ctx['titulo'] = 'Nuevo Paciente✅'
        return ctx


""" def nuevo(request):
    template_name = 'pacientes/nuevo.html'
    form = FormPaciente()
    message = ""
    if request.method == 'POST':
        form = FormPaciente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes:lista')
        else:
            message = "No se pudo guardar de forma correcta el formulario"
            
    ctx = {
        'form': form,
        "message": message
    }
    return render(request, template_name, ctx) """