How to Create a New Django App for a Cookiecutter-Django-Based Project
======================================================================

.. index:: Heroku


1. Create the ``<name-of-the-app>`` app with the following command:

   ::

       python manage.py startapp <name-of-the-app>

2. Move the ``<name-of-the-app>`` directory to the ``<project_slug>`` directory.

3. Edit ``<project_slug>/<name-of-the-app>/apps.py`` and change 
   ``name = "<name-of-the-app>"`` to ``name = "<project_slug>.<name-of-the-app>"``.

4. Add ``"<project_slug>.<name-of-the-app>"`` to your ``LOCAL_APPS`` in `config/settings/base.py <https://github.com/cookiecutter/cookiecutter-django/blob/d3d19264d7236dc704273a555e3741b26d0f848a/%7B%7Bcookiecutter.project_slug%7D%7D/config/settings/base.py#L97>`_.

