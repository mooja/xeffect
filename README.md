# mooja-django-stack

A Django project layout and ansbile playbooks designed to deploy and configure
the project with minimum effort. In addition to installing the specified repository,
it will install the following:

* Nginx
* Gunicorn
* PostgreSQL
* Virtualenv


Default settings are stored in roles/role_name/vars/main.yml.

Environment-specific settings are in the env_vars directory.
