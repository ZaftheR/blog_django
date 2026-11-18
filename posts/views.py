
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Vista de la página de inicio
def inicio(request):
    return render(request, 'posts/inicio.html')


# Vista de la página Acerca de
def acerca(request):
    return render(request, 'posts/acerca.html')


# Vista para mostrar los posts publicados
def lista_posts(request):
    posts = Post.objects.filter(
        estado="publicado"
    ).order_by("-fecha_creacion")

    context = {
        "posts": posts
    }

    return render(request, 'posts/lista_posts.html', context)


# Vista para mostrar el detalle de un post
def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'posts/detalle_post.html', {
        'post': post
    })


# Vista para crear un nuevo post
@login_required
def crear_post(request):
    if request.method == 'POST':
        formulario = PostForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_posts')
    else:
        formulario = PostForm()

    return render(request, 'posts/post_form.html', {
        'formulario': formulario,
        'titulo_pagina': 'Crear publicación'
    })


# Vista para editar un post existente
@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        formulario = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_post', post_id=post.id)
    else:
        formulario = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {
        'formulario': formulario,
        'titulo_pagina': 'Editar publicación'
    })


# Vista para eliminar un post
@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')

    return render(request, 'posts/post_confirm_delete.html', {
        'post': post
    })
