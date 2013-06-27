web: gunicorn mobible.wsgi
celery: python manage.py celery worker --concurrency=1 --beat
