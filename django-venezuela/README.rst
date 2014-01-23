django_venezuela
================

Aplicación en Django que contiene estados, ciudades, municipios y parroquias de Venezuela basada en https://github.com/marydn/venezuela-sql


Quick start
-----------
1. Instala el paquete django-venezuela con el comando `pip install django-venezuela`

2. Agrega "venezuela" al setting INSTALLED_APPS en el settings.py::

    INSTALLED_APPS = (
        ...
        'venezuela',
    )

3. Sincroniza el modelo de datos `python manage.py syncdb`

4. Corre las migraciones con el comando `python manage.py migrate` para crear los modelos Estado, Ciudad, Municipio y Parroquia.

