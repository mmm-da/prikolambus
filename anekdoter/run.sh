python wait_postgres.py
  python manage.py makemigrations anekdoter 
  python manage.py migrate
gunicorn anekdoter.wsgi:application --bind 0.0.0.0:8000