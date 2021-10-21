# Ourgram
A django application replicating the baasic features of Instagram

## Features
- Django 3.0+
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.

## Known Bugs
Comment functionality not working

## Environment Variables
```SECRET_KEY=XXX
DEBUG=True
DB_NAME='clonegram'
DB_USER='postgres'
DB_PASSWORD='XXXX
DB_HOST='127.0.0.1'
MODE='prod'
ALLOWED_HOSTS='.localhost','.herokuapp.com','.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=os.config('SECRET_KEY')
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used

## Versioning

We use [Git](https://git-scm.com/) for versioning. 


## Authors

* *Don Moses** - *Initial work* 
