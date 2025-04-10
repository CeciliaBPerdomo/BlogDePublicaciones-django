from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    # Obtener el valor de la búsqueda desde la URL
    busqueda = request.GET.get('busqueda', None)
    if busqueda:
        post_list = Post.objects.filter(titulo__icontains=busqueda)
    else:
        # Obtener todas las publicaciones de la base de datos
        post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'posts': post_list})

def post_create(request):
    if request.method == 'POST':
        # Procesar el formulario de creación de publicación
        form = PostForm(request.POST)
        if form.is_valid():
            # Guardar la nueva publicación en la base de datos
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect('blog:post_list')  # Redirigir a la lista de publicaciones después de crear una
            else:
                form.add_error(None, "Debes iniciar sesión para crear una publicación.")
    else:
        # Mostrar el formulario de creación de publicación
        form = PostForm()
    return render(request, 'blog/post_create.html', context={'form': form})