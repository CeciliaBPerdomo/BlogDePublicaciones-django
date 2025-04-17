<h1 align="center">
Blog de novedades
</h1>

<p align="center">
    <img src="myAvatar.png">
</p>

<p align="center">
    by Cecilia 💛 Perdomo
</p>

## Pasos para la instalación
- python -m venv .venv
- .venv\Scripts\activate
- pip install django
- django-admin startproject proyecto .
- crea la base de datos: python manage.py migrate
    - 🧠 **Tip extra**: Si agregás o modificás un modelo, siempre tenés que correr makemigrations y migrate, así Django sabe qué cambios reflejar en la base de datos.
        - python manage.py makemigrations --> (None)
        - python manage.py migrate
- levanta el servidor: **python manage.py runserver**
- crear app: python manage.py startapp blog
- python manage.py shell
    - from blog.models import Post
    - post = Post(titulo="Python", contenido="El lenguaje perfecto 4x4")
    - post.save()
- crear usuario administrador: python manage.py createsuperuser


## Borrar el .venv
- `git rm -r --cached venv`
- `git commit -m "Eliminando venv del índice de Git"`
- `git add .gitignore`
- `git commit -m "Actualizando .gitignore"`