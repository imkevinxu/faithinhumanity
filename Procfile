web: python manage.py collectstatic --noinput; newrelic-admin run-program gunicorn faithinhumanity.wsgi
worker: python manage.py tweet_scraper