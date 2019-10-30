# Backend - Face-recognition Based Attendance Taking System

## Setup

### Docker (Recommended)

make sure docker and docker-compose are installed

- mac: https://docs.docker.com/docker-for-mac/install/

under the project direction run

```sh
docker-compose up
```

The docker compose will automatically pull the required images and config them. (ref: docker-compose.yml)

After building (first time may take longer time),
you should see the backend is started at port 8000.

### Virtualenv (deprecated)

First, make sure you have `python3` installed.
Second, you need to start redis server, posgreSQL server, and celery workers

Using `virtualenv` is recommended. To create and activate a `virtualenv`:

```sh
virtualenv env
source env/bin/activate
```

To install all required packages, run

```sh
pip install -r requirements.txt
```

To start the development server, run

```sh
python manage.py. runserver
```

## Test

run tests

```
$ python manage.py test
```

run coverage

```
$ coverage run manage.py test
$ coverage report
```

generate html report

```
$ coverage run manage.py test && coverage html
```

open htmlcov/index.html
