web: gunicorn ordersite.wsgi
celery: celery worker -A ordersite -l info -c 4
worker: celery -A orderform.tasks worker -B --loglevel=info