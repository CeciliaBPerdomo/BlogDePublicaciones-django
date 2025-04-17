from django.views.generic import ListView, DetailView, DeleteView,CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, Avatar
from .forms import PostForm, EditUserForm, AvatarForm

from django.contrib.auth.decorators import login_required

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

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset

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

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')  # Redirigir a la lista de publicaciones después de crear una

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para crear una publicación.")
            return self.form_invalid(form)
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    #template_name = 'blog/post_update.html'
    success_url = reverse_lazy('blog:post_list')  # Redirigir a la lista de publicaciones después de actualizar una

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para actualizar una publicación.")
            return self.form_invalid(form)
        return super().form_valid(form)
class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'
    # context_object_name = 'post'

class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')  # Redirigir a la lista de publicaciones después de eliminar

def perfil(request):
    return render(request, 'blog/perfil.html')

@login_required
def editar_Perfil(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else: 
            avatar_form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect('blog:perfil')
    else:   
        form = EditUserForm(instance=request.user)
        if hasattr(request.user, 'avatar'):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(request, 'blog/editar_perfil.html', {'form': form, 'avatar_form': avatar_form})