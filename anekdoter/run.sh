#/bin/bash 
python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --no-input && gunicorn anekdoter.wsgi:application --bind 0.0.0.0:8000 --timeout 500