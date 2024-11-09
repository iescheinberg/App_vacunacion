from django.shortcuts import render, redirect
from .models import Usuario
from .forms import FormUsuario, FormUser


def nuevo(request):
    template_name = 'usuarios/nuevo.html'
    form = FormUser()
    message = ""
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:lista')
        else:
            message = "No se pudo guardar de forma correcta el formulario"
            
    ctx = {
        'form': form,
        "message": message
    }
    return render(request, template_name, ctx)
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    
    
    """ usuarios = Usuario.objects.filter(id=1)
    print("TODOS LOS USUARIOS")
    print(usuarios)
    print(usuarios.query)
    print("long:", len(usuarios))
    print("long:", usuarios.count())
    for us in usuarios:
        print(us) """
    
    ctx = {
        "usuarios": usuarios
    }
    return render(request, 'usuarios/lista.html', ctx)