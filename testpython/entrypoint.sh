#!/bin/bash

  set -e

  source /env/bin/activate

    if [ $1  == 'gunicorn' ]; then

      exec gunicorn testpyton.wsgi:application 0.0.0.0:8000 -b

    else

      exec python manage.py runserver  0.0.0.0:8000


    fi