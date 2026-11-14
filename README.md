# Blog Django

## Descripción

Proyecto base de un blog web desarrollado con Python y Django como parte de la Preentrega 7 de Coderhouse.

El proyecto contiene la estructura inicial de Django y una aplicación llamada `posts`, que se utilizará para gestionar las publicaciones del blog en futuras etapas.

## Tecnologías utilizadas

- Python
- Django 6.1.3
- SQLite

## Instalación

**1. Clonar el repositorio**

```bash
git clone https://github.com/ZaftheR/blog_django.git
```

**2. Entrar a la carpeta del proyecto**

```bash
cd blog_django
```

**3. Crear un entorno virtual**

```bash
python -m venv venv
```

**4. Activar el entorno virtual (Windows PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**5. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**6. Configurar la clave de Django**

En PowerShell, ejecutar:

```powershell
$env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Este comando genera una clave para utilizar Django de manera local. Debe ejecutarse nuevamente al abrir una nueva terminal.

**7. Iniciar el servidor**

```bash
python manage.py runserver
```

**8. Abrir el proyecto en el navegador**

http://127.0.0.1:8000/

## Aplicación principal

- `posts`: aplicación creada para gestionar las publicaciones del blog en futuras entregas.
