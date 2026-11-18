from django.shortcuts import render, redirect
from django.db import transaction

from .forms import RegistroForm, PerfilForm
from .models import Perfil

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404



# Vista para registrar nuevos usuarios
def registro(request):

    if request.method == 'POST':
        formulario = RegistroForm(request.POST)

        if formulario.is_valid():
            with transaction.atomic():
                usuario = formulario.save()

                # Crear un perfil para el nuevo usuario
                Perfil.objects.create(user=usuario)

            return redirect('login')

    else:
        formulario = RegistroForm()

    return render(request, 'accounts/registro.html', {
        'formulario': formulario
    })


# Vista para mostrar el perfil del usuario autenticado
@login_required
def perfil(request):

    perfil_usuario = get_object_or_404(
        Perfil,
        user=request.user
    )

    return render(request, 'accounts/perfil.html', {
        'perfil': perfil_usuario
    })


# Vista para editar el perfil del usuario autenticado
@login_required
def editar_perfil(request):

    perfil_usuario, creado = Perfil.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        formulario = PerfilForm(
            request.POST,
            request.FILES,
            instance=perfil_usuario
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')

    else:
        formulario = PerfilForm(instance=perfil_usuario)

    return render(request, 'accounts/editar_perfil.html', {
        'formulario': formulario
    })


