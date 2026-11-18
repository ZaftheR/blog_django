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
- Pillow 13.0.0

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

---

## Preentrega 10 - CRUD de Posts con Imágenes en Django

En esta etapa se implementó un sistema CRUD completo para gestionar publicaciones desde la interfaz web del blog, incorporando formularios dinámicos y soporte para imágenes.

### Modelo Post con imágenes

Se agregó al modelo `Post`, ubicado en `posts/models.py`, el campo:

```python
imagen = models.ImageField(
    upload_to='posts/',
    null=True,
    blank=True
)
```

Este campo permite asociar una imagen opcional a cada publicación, manteniendo la compatibilidad con los registros existentes.

Para actualizar la base de datos se ejecutaron:

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Formulario ModelForm

Se creó el archivo `posts/forms.py`, que contiene la clase `PostForm`, basada en `forms.ModelForm`.

El formulario permite completar los campos:

- Título.
- Contenido.
- Autor.
- Estado.
- Imagen.

Las vistas de creación y edición utilizan `request.POST` y `request.FILES` para procesar tanto los datos de texto como las imágenes.

El template `post_form.html` utiliza `method="POST"`, `enctype="multipart/form-data"` y `{% csrf_token %}`.

### Operaciones CRUD

Se implementaron las siguientes funcionalidades:

| Operación | Descripción | Ruta |
|---|---|---|
| Create | Crear publicaciones con imágenes | `/posts/crear/` |
| Read | Listar publicaciones publicadas | `/posts/` |
| Read | Consultar el detalle de un post | `/posts/<id>/` |
| Update | Editar publicaciones e imágenes | `/posts/<id>/editar/` |
| Delete | Eliminar publicaciones con confirmación | `/posts/<id>/eliminar/` |

Las rutas utilizan el identificador numérico de cada publicación.

El listado principal muestra únicamente publicaciones con estado `publicado`, ordenadas desde la más reciente.

### Configuración de archivos multimedia

Se incorporaron las siguientes configuraciones en `blog_project/settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Las imágenes cargadas se almacenan en el directorio `media/posts/`.

En `blog_project/urls.py` se configuró el acceso a los archivos multimedia durante el desarrollo local, utilizando `static()` cuando `DEBUG` está habilitado.

Los templates verifican si una publicación tiene imagen antes de intentar mostrarla.

### Dependencias

Para trabajar con el campo `ImageField` se instaló Pillow.

El entorno utilizado incluye:

- Python 3.12.10.
- Django 6.1.3.
- Pillow 13.0.0.
- SQLite.

Las dependencias están registradas en `requirements.txt`.

Para instalarlas:

```powershell
python -m pip install -r requirements.txt
```

### Templates incorporados

Se crearon o actualizaron los siguientes archivos:

- `lista_posts.html`: listado de publicaciones con enlaces de creación y detalle.
- `detalle_post.html`: visualización completa de una publicación.
- `post_form.html`: formulario utilizado para crear y editar publicaciones.
- `post_confirm_delete.html`: confirmación antes de eliminar un post.

Todos mantienen la herencia desde `posts/base.html`.

También se incorporaron estilos CSS para presentar los enlaces de creación y visualización como botones azules con esquinas redondeadas.

### Pruebas realizadas

Se comprobaron las siguientes funcionalidades:

1. Creación de publicaciones con imágenes.
2. Visualización de imágenes en el listado y en el detalle.
3. Edición de publicaciones existentes.
4. Actualización y reemplazo de imágenes.
5. Creación, edición y eliminación de una publicación de prueba.
6. Confirmación previa a la eliminación.
7. Navegación entre las páginas del blog.
8. Funcionamiento de las rutas y templates.
9. Aplicación de migraciones en SQLite.
10. Verificación de la configuración mediante `python manage.py check`.

Las pruebas se realizaron utilizando el servidor local de Django.

### Cómo probar el CRUD

Una vez instalado el proyecto, configurada la variable `DJANGO_SECRET_KEY` y aplicadas las migraciones, iniciar el servidor:

```powershell
python manage.py runserver
```

Ingresar a:

http://127.0.0.1:8000/posts/

Seleccionar **Crear publicación**, completar el formulario, elegir una imagen JPG o PNG y guardar.

La publicación debe aparecer en el listado si se seleccionó el estado `Publicado`.

Desde el detalle se puede editar la publicación, cambiar su imagen o acceder a la confirmación de eliminación.

La base de datos SQLite es local y no se incluye en el repositorio. Por lo tanto, una instalación nueva comenzará sin publicaciones cargadas.

### Alcance

El proyecto está preparado para ejecutarse en un entorno de desarrollo local.

Esta preentrega no incorpora autenticación ni permisos para proteger las operaciones de creación, edición y eliminación. Estas funcionalidades deberán protegerse antes de publicar la aplicación en Internet.

---

## Estado de la Preentrega 10

Se completó la implementación del modelo Post con imágenes, el formulario ModelForm, las operaciones CRUD, la configuración multimedia y las pruebas funcionales.

El proyecto continúa utilizando el mismo repositorio de las entregas anteriores.

Repositorio: https://github.com/ZaftheR/blog_django

---

## Preentrega 11 - Autenticación, Usuarios y Perfil en Django

En esta etapa se incorporó un sistema de autenticación y gestión de usuarios al blog, utilizando las herramientas nativas de Django.

Los visitantes pueden registrarse, iniciar sesión y cerrar sesión. Cada usuario tiene un perfil propio con biografía, enlace web opcional y avatar.

También se implementó la protección de las operaciones CRUD para que solamente los usuarios autenticados puedan crear, editar y eliminar publicaciones.

### Aplicación accounts

Se creó una nueva aplicación llamada `accounts` para organizar las funcionalidades relacionadas con los usuarios.

Sus archivos principales son:

- `models.py`: contiene el modelo Perfil.
- `forms.py`: contiene los formularios de registro y edición del perfil.
- `views.py`: contiene las vistas de registro, visualización y edición del perfil.
- `urls.py`: define las rutas de autenticación y perfiles.
- `admin.py`: registra el modelo Perfil en el administrador.
- `templates/accounts/`: contiene las páginas HTML de autenticación y perfil.

### Registro de usuarios

Se implementó `RegistroForm`, un formulario personalizado basado en `UserCreationForm` de Django.

El formulario permite ingresar:

- Nombre de usuario.
- Correo electrónico.
- Contraseña.
- Confirmación de contraseña.

La vista `registro()` valida los datos, crea el usuario y genera automáticamente su perfil asociado mediante `Perfil.objects.create(user=usuario)`.

Ambas operaciones se realizan dentro de una transacción para mantener la consistencia de los datos.

Ruta de registro:

`/accounts/registro/`

### Inicio y cierre de sesión

Se implementaron las vistas nativas de autenticación de Django:

- `LoginView`: permite iniciar sesión.
- `LogoutView`: permite cerrar sesión.

Las rutas disponibles son:

- `/accounts/login/`: inicio de sesión.
- `/accounts/logout/`: cierre de sesión mediante POST.

En `settings.py` se configuraron las siguientes redirecciones:

```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'lista_posts'
LOGOUT_REDIRECT_URL = 'lista_posts'
```

Después de iniciar o cerrar sesión, el usuario es redirigido al listado de publicaciones.

### Modelo Perfil

Se creó el modelo `Perfil` en `accounts/models.py`.

Este modelo se relaciona con el usuario de Django mediante `OneToOneField`, permitiendo que cada cuenta tenga un único perfil asociado.

Contiene los siguientes campos:

- `user`: usuario asociado al perfil.
- `biografia`: descripción personal opcional.
- `link_web`: enlace web opcional.
- `avatar`: imagen de perfil opcional.

El avatar utiliza `ImageField` y se almacena dentro de `media/avatares/`.

Se generaron y aplicaron las migraciones correspondientes mediante:

```powershell
python manage.py makemigrations accounts
python manage.py migrate
```

El modelo Perfil también fue registrado en el panel administrativo de Django.

### Visualización y edición del perfil

Cada usuario autenticado puede consultar su información desde:

`/accounts/perfil/`

La página muestra:

- Nombre de usuario.
- Correo electrónico.
- Biografía.
- Enlace web, cuando existe.
- Avatar, cuando existe.

La edición está disponible en:

`/accounts/perfil/editar/`

Se creó `PerfilForm`, basado en `ModelForm`, para modificar la biografía, el enlace web y el avatar.

La vista de edición utiliza `request.POST`, `request.FILES` e `instance=perfil_usuario` para guardar los cambios en el perfil existente.

El formulario HTML incluye `enctype="multipart/form-data"` para permitir la carga de imágenes.

### Protección de publicaciones

Se incorporó el decorador `@login_required` en las siguientes vistas de `posts/views.py`:

- `crear_post()`
- `editar_post()`
- `eliminar_post()`

Los usuarios que no iniciaron sesión son redirigidos automáticamente al formulario de autenticación.

Por ejemplo, al intentar acceder a `/posts/crear/`, un visitante es redirigido a:

`/accounts/login/?next=/posts/crear/`

Las vistas de listado y detalle de publicaciones continúan siendo públicas.

### Navegación dinámica

Se actualizó el template `posts/base.html` para mostrar diferentes opciones según el estado de autenticación.

**Visitantes no autenticados:**

- Inicio.
- Acerca de.
- Publicaciones.
- Iniciar sesión.
- Registrarse.

**Usuarios autenticados:**

- Inicio.
- Acerca de.
- Publicaciones.
- Mi perfil.
- Crear post.
- Cerrar sesión.

El cierre de sesión se realiza mediante un formulario POST con protección CSRF.

### Configuración multimedia

Se reutilizó la configuración de la Preentrega 10:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Las imágenes de publicaciones se guardan en `media/posts/` y los avatares en `media/avatares/`.

La visualización de archivos multimedia está habilitada durante el desarrollo local.

### Pruebas realizadas

Se comprobaron las siguientes funcionalidades:

1. Registro de un usuario nuevo.
2. Creación automática del perfil asociado.
3. Inicio de sesión con las credenciales registradas.
4. Redirección al listado después del login.
5. Visualización del perfil del usuario autenticado.
6. Edición del perfil y carga de avatar.
7. Visualización correcta de la imagen de perfil.
8. Cierre de sesión y actualización del menú.
9. Redirección al login al intentar crear publicaciones sin autenticación.
10. Protección de las vistas de edición y eliminación.
11. Acceso público al listado y al detalle de publicaciones.
12. Conservación del CRUD con imágenes de la Preentrega 10.

Las comprobaciones se realizaron en el entorno de desarrollo local utilizando Django y SQLite.

### Cómo probar la autenticación

Después de instalar las dependencias, configurar `DJANGO_SECRET_KEY`, aplicar las migraciones y ejecutar `python manage.py runserver`:

1. Ingresar a `/accounts/registro/` y crear una cuenta.
2. Iniciar sesión desde `/accounts/login/`.
3. Abrir `/accounts/perfil/` para consultar el perfil.
4. Utilizar `/accounts/perfil/editar/` para modificar la biografía y subir un avatar.
5. Crear una publicación desde `/posts/crear/`.
6. Cerrar sesión desde el menú.
7. Comprobar que las operaciones de creación, edición y eliminación requieren autenticación.

La base de datos SQLite y las imágenes cargadas durante el desarrollo se mantienen localmente y no se incluyen en el repositorio.

### Estado de la Preentrega 11

Se implementó la autenticación de usuarios, el registro personalizado, el modelo Perfil con relación OneToOne, la edición de biografía y avatar, la navegación condicional y la protección de las operaciones CRUD.

El proyecto continúa utilizando el mismo repositorio de GitHub de las entregas anteriores.

Repositorio: https://github.com/ZaftheR/blog_django