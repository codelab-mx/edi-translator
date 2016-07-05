EDI Translator V. 0.5.1
=============

Software para traducción de documentos en formato EDI

    Todas las herramientas utilizadas para la creación de este proyecto son OpenSource.

Características:
-------

0. Administración y logeo seguro
0. Decodificación de ficheros en texto plano con codificación edi
0. Codificación de ficheros en texto plano con codificación edi
0. Registro de usuarios


Más información en <http://consulta-its.com>`.

RAMAS
-------
Master - Es la rama principal. Contiene el repositorio que se encuentra publicado en producción, por lo que debe estar siempre estable.

Development - Rama de integración, todas las nuevas funcionalidades se deben integrar en esta rama.

Features - Rama de nuevas características, cada nueva característica debe tener sus propias ramas las cuales al finalizar deberán añadirse al canal Development

Hotfix - Son bugs que surgen en producción, por lo que se deben arreglar y publicar de forma urgente.

Requisitos
-----------

Un servidor Linux / Unix o Windows con Nginx y Django como framework

Inicio rápido
```
pip install django
```
En el directorio principal del software con django previamente instalado
```
python manage.py runserver
```

	Acceder por medio de localhost:8000/ en el navegador

Soporte
------------
Para ayuda sobre como clonar el proyecto y editarlo consulte con http://codelab.mx


Soporte Adicional
------------

Este proyecto es creado por 'Codelab MX' en colaboración con Consulta-ITS
Si se tiene alguna duda del funcionamiento del mismo favor de contactar a:
ftejeda@consulta-its.com