from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as login_django

def mi_pagina_inicio(request):
    lista_usuarios = [
        {'nombre': 'Juan', 'apellido': 'Perez'},
        {'nombre': 'Maria', 'apellido': 'Garcia'},
        {'nombre': 'Pedro', 'apellido': 'Lopez'}
    ]
    contexto = {
        "todos_los_usuarios": lista_usuarios
    }
    return render(request, 'mi_pagina_inicio.html', contexto)

# Se corto de aqui la funcion de lista_usuarios



def login(request):
    # print("method", request.method)
    # print("============================")
    # print(request)
    # print(request.__class__.__name__)
    # print(request.__dict__)
    se_autentico = False
    salio_mal = True
    username = ""
    if request.method == "POST":
        username = request.POST.get('username', default=None)
        password = request.POST.get('password', default=None)
        usuario = authenticate(request, username=username, password=password)
        se_autentico = True
        if usuario:
            salio_mal = False
            login_django(request, usuario)
            return redirect("inicio")
        else:
            print("autenticacion mal")
    ctx = {
        "se_autentico": se_autentico, 
        "salio_mal": salio_mal,
        "username": username
    }
    return render(request, 'login.html', ctx)