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

3. Crea la base de datos con soporte UTF8, en mysql la creamos de la siguiente manera::
    CREATE DATABASE db_name CHARACTER SET utf8 COLLATE utf8 utf8_general_ci;

4. Sincroniza el modelo de datos `python manage.py syncdb`
