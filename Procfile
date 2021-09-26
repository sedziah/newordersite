web: gunicorn ordersite.wsgi

celery -A ordersite worker -l info --pool=solo