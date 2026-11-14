# Blog Django

## Descripción

Proyecto de un blog web desarrollado con Python y Django como parte de las Preentregas 7 y 8 del curso Python Inicial de Coderhouse.

En la Preentrega 7 se creó la estructura inicial del proyecto Django y la aplicación `posts`.

En la Preentrega 8 se desarrolló la primera interfaz visual del blog utilizando HTML, CSS, vistas y rutas de Django.

Actualmente, el sitio cuenta con una página de inicio, una página Acerca de y un menú de navegación que permite desplazarse entre ambas.

## Tecnologías utilizadas

- Python
- Django 6.1.3
- HTML5
- CSS3
- SQLite (configurado por defecto en Django)
- Git y GitHub

## Funcionalidades implementadas

- Página de inicio con un mensaje de bienvenida.
- Página Acerca de con información sobre el autor y el objetivo del blog.
- Menú de navegación entre ambas páginas.
- Plantilla principal `base.html`.
- Herencia de templates utilizando `{% extends %}` y `{% block content %}`.
- Vistas basadas en funciones que utilizan `render()`.
- Rutas organizadas mediante `path()` e `include()`.
- Archivos estáticos con estilos CSS personalizados.

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

### 6. Configurar la clave secreta de Django

Por seguridad, la clave secreta no está incluida directamente en el código del proyecto.

En Windows PowerShell, ejecutar:

```powershell
$env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Esta variable se configura para la sesión actual de la terminal. Si se abre una terminal nueva, será necesario configurarla nuevamente.

### 7. Iniciar el servidor de Django

```bash
python manage.py runserver
```

### 8. Abrir el sitio en el navegador

Página de inicio:

http://127.0.0.1:8000/

Página Acerca de:

http://127.0.0.1:8000/acerca/

## Aplicación principal: posts

La aplicación `posts` contiene las vistas, rutas, templates y archivos estáticos del blog.

### Vistas

En `posts/views.py` se encuentran las funciones:

- `inicio()`: muestra la página principal.
- `acerca()`: muestra la información sobre el blog.

Ambas utilizan la función `render()` de Django.

### Rutas

En `posts/urls.py` se encuentran las rutas de Inicio y Acerca de.

Estas rutas están conectadas con el proyecto principal mediante `include()` en `blog_project/urls.py`.

### Templates

Los archivos HTML se encuentran en `posts/templates/posts/`.

- `base.html`: plantilla principal que contiene la estructura HTML5, el encabezado, el menú de navegación y el pie de página.
- `inicio.html`: página principal del blog.
- `acerca.html`: página con información sobre el autor y el propósito del sitio.

Las páginas `inicio.html` y `acerca.html` heredan su estructura de `base.html`.

### Archivos estáticos

El archivo `estilos.css` se encuentra en:

`posts/static/posts/css/estilos.css`

Contiene estilos para:

- Tipografía.
- Colores del sitio.
- Encabezado.
- Menú de navegación.
- Contenido principal.
- Títulos.
- Pie de página.

El CSS se vincula desde `base.html` utilizando `{% load static %}` y la etiqueta `{% static 'posts/css/estilos.css' %}`.

## Pruebas realizadas

Se realizaron las siguientes verificaciones para comprobar el funcionamiento del proyecto.

### 1. Comprobación de Django

Se ejecutó:

```bash
python manage.py check
```

Resultado obtenido:

```text
System check identified no issues (0 silenced).
```

### 2. Ejecución del servidor

Se ejecutó:

```bash
python manage.py runserver
```

El servidor inició correctamente y permitió acceder al sitio desde el navegador.

### 3. Página de inicio

Se comprobó que la dirección `http://127.0.0.1:8000/` muestra la página de bienvenida.

### 4. Página Acerca de

Se comprobó que la dirección `http://127.0.0.1:8000/acerca/` muestra la información del blog.

### 5. Navegación

Se verificó que los enlaces del menú permiten navegar entre Inicio y Acerca de sin errores.

### 6. Archivos estáticos

Se utilizaron las herramientas de desarrollador del navegador para comprobar que `estilos.css` se carga correctamente.

Se verificó una respuesta HTTP `200` y que los estilos visuales se aplican en ambas páginas.

## Estado del proyecto

El proyecto cumple con los requisitos principales de la Preentrega 8:

- Estructura de templates y archivos estáticos.
- Herencia HTML con `base.html`.
- Vistas con `render()`.
- Rutas conectadas mediante `include()`.
- Navegación funcional.
- Estilos CSS personalizados.

En futuras etapas se podrán incorporar publicaciones dinámicas, modelos de datos, formularios y otras funcionalidades.

## Autor

Proyecto desarrollado como parte del curso Python Inicial de Coderhouse.

## Repositorio

https://github.com/ZaftheR/blog_django