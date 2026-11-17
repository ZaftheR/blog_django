# Blog Django

## Descripción

Proyecto de un blog web desarrollado con Python y Django como parte de las Preentregas 7 y 8 del curso Python Inicial de Coderhouse.

En la Preentrega 7 se creó la estructura inicial del proyecto Django y la aplicación `posts`, configurando el entorno de desarrollo, las dependencias y los archivos principales.

En la Preentrega 8 se desarrolló la primera interfaz visual del blog utilizando HTML5, CSS3, vistas, rutas y herencia de templates de Django.

Actualmente, el sitio cuenta con una página de inicio, una página Acerca de y un menú de navegación que permite desplazarse entre ambas.

## Tecnologías utilizadas

- Python 3.12
- Django 6.1.3
- HTML5
- CSS3
- SQLite
- Git y GitHub

## Requisitos previos

Para ejecutar el proyecto se necesita:

- Python 3.12 o superior, compatible con la versión de Django utilizada.
- pip para instalar las dependencias.
- Git para clonar el repositorio.
- Una terminal de comandos.
- Un navegador web.

## Funcionalidades implementadas

- Página de inicio con un mensaje de bienvenida.
- Página Acerca de con información sobre el autor y el propósito del blog.
- Menú de navegación entre ambas páginas.
- Plantilla principal `base.html`.
- Herencia de templates mediante `{% extends %}` y `{% block content %}`.
- Vistas basadas en funciones que utilizan `render()`.
- Rutas organizadas mediante `path()` e `include()`.
- Archivos estáticos con estilos CSS personalizados.
- Configuración de SQLite y migraciones iniciales de Django.

## Estructura del proyecto

```text
blog_django/
│
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    │   └── __init__.py
    │
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       └── acerca.html
    │
    └── static/
        └── posts/
            └── css/
                └── estilos.css
```

## Descripción de las carpetas y archivos principales

### Carpeta blog_project

Contiene la configuración general del proyecto Django.

- `settings.py`: configuración del proyecto, aplicaciones instaladas, idioma, zona horaria y base de datos.
- `urls.py`: rutas principales del proyecto.
- `asgi.py`: configuración para servidores ASGI.
- `wsgi.py`: configuración para servidores WSGI.

### Carpeta posts

Es la aplicación principal del blog.

- `admin.py`: configuración del administrador de Django.
- `apps.py`: configuración de la aplicación.
- `models.py`: archivo destinado a los futuros modelos de datos.
- `tests.py`: archivo destinado a las pruebas automatizadas.
- `views.py`: contiene las funciones que muestran las páginas HTML.
- `urls.py`: define las rutas de la aplicación.

### Carpeta migrations

Contiene los archivos de migraciones de la aplicación.

Las migraciones permiten administrar los cambios en la estructura de la base de datos.

### Carpeta templates

Contiene los archivos HTML del sitio.

- `base.html`: plantilla principal con el encabezado, menú de navegación y pie de página.
- `inicio.html`: página principal del blog.
- `acerca.html`: página con información sobre el autor y el objetivo del sitio.

Las páginas `inicio.html` y `acerca.html` heredan su estructura de `base.html`.

### Carpeta static

Contiene los archivos estáticos utilizados para el diseño del sitio.

El archivo `posts/static/posts/css/estilos.css` define los estilos visuales del blog.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/ZaftheR/blog_django.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd blog_django
```

### 3. Crear un entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene las dependencias necesarias para ejecutar el proyecto y está guardado con codificación UTF-8.

### 6. Configurar la clave secreta de Django

Por seguridad, la clave secreta del proyecto no se encuentra escrita directamente en el código.

En Windows PowerShell, ejecutar:

```powershell
$env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Esta variable se configura para la sesión actual de la terminal. Si se abre una terminal nueva, será necesario configurarla nuevamente.

### 7. Aplicar las migraciones de la base de datos

Antes de iniciar el servidor, ejecutar:

```bash
python manage.py migrate
```

Este comando prepara las tablas de la base de datos necesarias para las aplicaciones de Django.

Si las migraciones ya fueron aplicadas, puede aparecer el mensaje:

```text
No migrations to apply.
```

Esto indica que no hay migraciones pendientes.

### 8. Comprobar la configuración de Django

```bash
python manage.py check
```

Si la configuración es correcta, Django mostrará:

```text
System check identified no issues (0 silenced).
```

### 9. Iniciar el servidor

```bash
python manage.py runserver
```

### 10. Abrir el sitio en el navegador

Página de inicio:

http://127.0.0.1:8000/

Página Acerca de:

http://127.0.0.1:8000/acerca/

## Aplicación principal: posts

La aplicación `posts` contiene las vistas, rutas, templates y archivos estáticos del blog.

### Vistas

En `posts/views.py` se encuentran dos funciones:

- `inicio()`: muestra la página principal.
- `acerca()`: muestra la información sobre el blog.

Ambas utilizan la función `render()` de Django para devolver los templates HTML correspondientes.

### Rutas

En `posts/urls.py` se definen las rutas de Inicio y Acerca de mediante `path()`.

Estas rutas están conectadas con el proyecto principal mediante `include()` en `blog_project/urls.py`.

### Herencia de templates

El archivo `base.html` contiene la estructura HTML5 general del sitio, incluyendo el menú de navegación.

Las páginas `inicio.html` y `acerca.html` utilizan `{% extends 'posts/base.html' %}` para reutilizar esa estructura.

El contenido particular de cada página se coloca dentro del bloque `{% block content %}`.

### Archivos estáticos

El archivo `estilos.css` se encuentra en:

`posts/static/posts/css/estilos.css`

Contiene reglas para:

- Tipografía.
- Colores generales.
- Encabezado.
- Menú de navegación.
- Contenido principal.
- Títulos.
- Pie de página.

El CSS se vincula desde `base.html` utilizando `{% load static %}` y `{% static 'posts/css/estilos.css' %}`.

## Seguridad y control de versiones

El proyecto utiliza un archivo `.gitignore` para evitar incorporar archivos innecesarios o privados al repositorio.

Entre los elementos ignorados se encuentran:

- `venv/`: entorno virtual de Python.
- `__pycache__/`: archivos temporales de Python.
- `*.pyc`: archivos compilados de Python.
- `.env`: archivo de variables de entorno.
- `db.sqlite3`: base de datos local.

La configuración `SECRET_KEY` se obtiene desde una variable de entorno para evitar publicar una clave secreta en GitHub.

## Pruebas realizadas

### 1. Comprobación de Django

Se ejecutó:

```bash
python manage.py check
```

Resultado:

```text
System check identified no issues (0 silenced).
```

### 2. Verificación de migraciones

Se ejecutó:

```bash
python manage.py migrate
```

Resultado:

```text
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

Se comprobó que las migraciones estaban aplicadas correctamente.

### 3. Ejecución del servidor

Se ejecutó:

```bash
python manage.py runserver
```

El servidor inició correctamente después de configurar la variable de entorno `DJANGO_SECRET_KEY`.

### 4. Página de inicio

Se verificó que la dirección `http://127.0.0.1:8000/` muestra correctamente la página de bienvenida del blog.

### 5. Página Acerca de

Se verificó que la dirección `http://127.0.0.1:8000/acerca/` muestra la información sobre el blog y su autor.

### 6. Navegación

Se comprobó que los enlaces del menú permiten navegar entre Inicio y Acerca de sin errores.

### 7. Archivos estáticos

Se utilizaron las herramientas de desarrollador del navegador para comprobar que el archivo `estilos.css` carga correctamente.

Se verificó una respuesta HTTP `200` y que los estilos se aplican visualmente.

### 8. Codificación de requirements.txt

Se verificó que el archivo `requirements.txt` puede leerse correctamente utilizando codificación UTF-8.

### 9. Archivos temporales de Git

Se comprobó que el repositorio ya no mantiene archivos `__pycache__` ni `*.pyc` bajo seguimiento de Git.

## Estado del proyecto

El proyecto incluye las funcionalidades solicitadas en las Preentregas 7 y 8:

- Estructura inicial de Django.
- Aplicación `posts` registrada.
- Configuración de idioma y zona horaria.
- Configuración de la clave secreta mediante variable de entorno.
- Dependencias documentadas.
- Migraciones de Django aplicadas.
- Templates HTML con herencia.
- Vistas utilizando `render()`.
- Rutas conectadas mediante `include()`.
- Navegación funcional.
- Estilos CSS personalizados.

En futuras etapas se podrán incorporar modelos de publicaciones, formularios, operaciones CRUD y otras funcionalidades dinámicas.

## Autor

Proyecto desarrollado como parte del curso Python Inicial de Coderhouse.

## Repositorio de GitHub

https://github.com/ZaftheR/blog_django

## Preentrega 9 - Modelos y administración en Django

En esta etapa se incorporó la persistencia de publicaciones mediante SQLite y el ORM de Django.

### Modelo Post

Se creó el modelo `Post` en `posts/models.py`, con los siguientes campos:

- `titulo`: título de la publicación.
- `contenido`: texto de la publicación.
- `autor`: nombre del autor.
- `fecha_creacion`: fecha generada automáticamente con `auto_now_add=True`.
- `estado`: permite seleccionar borrador, publicado o archivado.

El modelo implementa el método `__str__()` para representar cada publicación mediante su título.

### Migraciones y base de datos

Para generar y aplicar las migraciones, ejecutar:

```powershell
python manage.py makemigrations
python manage.py migrate
```

La base de datos utiliza SQLite mediante el archivo local `db.sqlite3`, excluido del repositorio por `.gitignore`.

### Panel de administración

El modelo `Post` está registrado en `posts/admin.py` mediante una clase `PostAdmin`.

El administrador permite visualizar el título, autor, estado y fecha de creación de cada publicación, además de buscar y filtrar los registros.

Para crear una cuenta de administrador, ejecutar:

```powershell
python manage.py createsuperuser
```

Después de iniciar el servidor con `python manage.py runserver`, acceder a:

http://127.0.0.1:8000/admin/

Ingresar con el superusuario creado para administrar las publicaciones.

### Listado dinámico

Se incorporó la página de publicaciones:

http://127.0.0.1:8000/posts/

La vista `lista_posts()` consulta la base de datos mediante:

```python
Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
```

El template `lista_posts.html` utiliza `{% for post in posts %}` para mostrar dinámicamente el título, contenido, autor y fecha de las publicaciones.

Solamente se muestran los posts publicados, ordenados desde el más reciente.

### Pruebas realizadas

- Se generaron y aplicaron las migraciones del modelo Post.
- Se configuró correctamente el panel administrativo de Django.
- Se creó un superusuario y se comprobó el acceso a `/admin/`.
- Se cargaron tres publicaciones con distintos estados.
- Se verificó que `/posts/` muestra únicamente las publicaciones publicadas.
- Se mantuvieron las páginas Inicio y Acerca de, la herencia HTML y los estilos CSS de la Preentrega 8.

### Estructura incorporada

- `posts/models.py`: definición del modelo Post.
- `posts/admin.py`: configuración del panel administrativo.
- `posts/migrations/0001_initial.py`: migración inicial del modelo.
- `posts/views.py`: consulta de publicaciones mediante ORM.
- `posts/urls.py`: ruta del listado de publicaciones.
- `posts/templates/posts/lista_posts.html`: template dinámico del listado.