# django_ncsu

## Installation

Install python packages

```
pip install -r requirements.txt
```

Use following commands to set up the localhost debug servere

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

Find your debug server using a browser and http://127.0.0.1:8000 as an url.

If you want to run on a real host (not localhost) add your hostname to `ALLOWED_HOSTS` in mysite/settings.py and use uwsgi to launch it (explanations follow).
