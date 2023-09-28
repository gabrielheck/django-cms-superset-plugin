=====
Django CMS Superset Plugin
=====

Django CMS plugin for embedding Superset dashboards.

Quick start
-----------

1. Add "django_cms_superset_plugin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_cms_superset_plugin",
    ]

2. Run ``python manage.py makemigrations django_cms_superset_plugin`` to create the django_cms_superset_plugin migrations.

3. Run ``python manage.py migrate django_cms_superset_plugin`` to create the django_cms_superset_plugin models.

4. Start the development server and visit http://127.0.0.1:8000/admin/ to add/edit
new dashboards to your pages. The plugin name is identified as superset.

Key Features
-----------

- Add/modify multiple row level security filters
- Change dashboard width and height
- Toogle the display of dashboard elements title, tab, chart controls, and filters

Screenshots
-----------

https://a.imagem.app/oHncGS.png

Roadmap
-----------

- Support Jinja Templating to improve row level security filter clauses;
- Improve error handling;
- Tests and CI;
- Feel free to propose new ideas!
