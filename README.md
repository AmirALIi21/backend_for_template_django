# backend_for_template_django
this is a template with django for backend
first you have to download the postdgres driver for database and sign in ,then change your settings.py like this :
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'amir',
        'USER': 'postgres',
        'PASSWORD': '13801380',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
next open your command prompt and run these commands : cd C:\Program Files\PostgreSQL\<your_driver_version>\bin #this is a path to your db diver
                                                       pg_ctl start -D "C:\Program Files\PostgreSQL\<your_driver_version>\data" # to run the sever 
                                                       pg_ctl status -D "C:\Program Files\PostgreSQL\<your_driver_version>\data" # for server status
you can use this command to create your own db but remember to change the settings.py : CREATE DATABASE <your_db_name>;                                                      
note : as long as you keep the command prompt open , the server will stay running.
now you have to change your settings.py again for the dirs , change them like this :
STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'tsk1/static/tsk1'),
]
if you want you can create another superuser or just use mine : i think it was admin , 13801380
now run the server by typing : python manage.py runserver
