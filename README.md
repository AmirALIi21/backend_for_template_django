# backend_for_template_django
this is a template with django for backend
-------------------------------DATABASE_SETTINGS--------------------------------------
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
--------------------------------STATIC_FILES----------------------------------------
now you have to change your settings.py again for the dirs , change them like this :
STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'tsk1/static/tsk1'),
]
--------------------------------SEND_MAIL-------------------------------------------
to send email: first open git bash ( cause command prompt is already using for db server ), then use cd command to navigate to your project 
where manage.py is exist , then run the below command to run the server :
python -m smtpd -n -c DebuggingServer localhost:1025
now the server will be listening.(it shows nothing until you send an email)
keep the git bash open as long as you want to use the email function,
add this to your settings.py like this :
# SMTP server settings
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025  # Use the appropriate port for your SMTP server
EMAIL_USE_TLS = False  # Use TLS security
EMAIL_USE_SSL = False  # Use SSL security (choose one, either TLS or SSL)
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
now you can send an email and you can see it in the git bash terminal 
if you took your project on server then you have to change the settings with your actuall configurations.
--------------------------------------------------------------------------------------
if you want you can create another superuser or just use mine : i think it was admin , 13801380
now run the server by typing : python manage.py runserver
