SECRET_KEY = 'django-insecure-bd(2jq@rpq)u!_d75148+(kc*1ms+012&45k=ueogh7u^gq_&4'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone',
        'USER': 'root',
        'PASSWORD': 'password_123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}