from django import forms
from .models import Post, Avatar

# Par editar el formulario de usuario
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'estado']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'estado': 'Estado',
        }
        # help_texts = {
        #     'titulo': 'Ingrese el título de la publicación',
        #     'contenido': 'Ingrese el contenido de la publicación',
        #     'estado': 'Seleccione el estado de la publicación',
        # }
        error_messages = {
            'titulo': {
                'max_length': 'El título es demasiado largo.',
            },
            'contenido': {
                'required': 'Este campo es obligatorio.',
            },
        }

class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    first_name = forms.CharField(required=True, label='Nombre')
    last_name = forms.CharField(required=True, label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']