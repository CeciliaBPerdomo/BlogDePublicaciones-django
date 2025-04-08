from django import forms
from .models import Post

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
