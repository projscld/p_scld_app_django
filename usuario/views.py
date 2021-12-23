from django.shortcuts import redirect, render
from .models import Usuario
from.forms import UsuarioForm

# Create your views her

def listar_usuarios(request):
    usuario = Usuario.objects.all()
    return render(request, 'usuario/listar_usuarios.html', {'usuario' : usuario})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form =  UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/form_usuario.html', {'form': form})