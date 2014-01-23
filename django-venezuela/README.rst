django_venezuela
================

Aplicación en Django que contiene estados, ciudades, municipios y parroquias de Venezuela


Quick start
-----------

1. Agrega "venezuela" al setting INSTALLED_APPS en el settings.py::

    INSTALLED_APPS = (
        ...
        'venezuela',
    )

2. Sincroniza el modelo de datos `python manage.py syncdb`

3. Corre las migraciones con el comando `python manage.py migrate` para crear los modelos Estado, Ciudad, Municipio y Parroquia.