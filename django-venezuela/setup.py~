# -*- coding: utf-8 -*-
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-venezuela',
    version='0.4.1',
    packages=['venezuela'],
    include_package_data=True,
    license='GPL v2 License',
    description=u'Aplicación en Django que contiene los modelos de estados, ciudades, municipios y '
                u'parroquias de Venezuela.',
    long_description=README,
    url='http://rub3nc.wordpress.com/',
    author=u'Rubén Colina',
    author_email='ruben.colina@gmail.com',
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
)
