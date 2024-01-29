web: gunicorn BYT.wsgi
release: python manage.py migrate && python manage.py loaddata startup_fixtures.json
