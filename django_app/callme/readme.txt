# Resources
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django                                             Tutorial
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones                                                  Time Zones
# https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types                                          Model Field Types
# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models        Phone Number RegEx
# https://github.com/stefanfoulis/django-phonenumber-field/blob/master/phonenumber_field/tests.py               Alternative Phone Number (UPGRADE?)

# Activate Virtual Env
source bin/activate

# pip3 installs
pip3 install django


# Changes to tutorial
django_test -> django_app

# Migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Run server
python3 manage.py runserver

# Creat superuser
python3 manage.py createsuperuser

# user: cc
# email: dev+callme@cederskog.de
# pwd: S...5

