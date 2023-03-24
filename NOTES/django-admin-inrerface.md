STEPS
create django project (django-admin startproject <projectname>)

create django applications (as many as you want)

To access django admin interface, you need to create a superuser

python manage.py makemigrations (this commands identifies changes in model definition)

python manage.py migrate

To create superuser - python manage.py createsuperuser

Run application python manage.py runserver and go to http://home-url/admin

Django migrations
python manage.py makemigrations command needs to be executed whenever there is any change in models.py
python manage.py migrate command applies migrations created by above command