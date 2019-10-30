# Backend - Face-recognition Based Attendance Taking System

## Setup

### Docker

First, make sure docker and docker-compose are installed. For installation guide, visit [Docker Docs](https://docs.docker.com/) and select appropriate OS on the bottom of the page.

under the project root directory run

```sh
docker-compose up
```

The docker compose will automatically pull the required images and config them. (ref: docker-compose.yml)

After building (first time may take a longer time), the backend server will be ready at port `8000`.

### Django Super User and Admin Page

To create super users for `django`

```bash
docker-compose run web python manage.py createsuperuser
```

The admin page will be accessble at `http://localhost:8000/admin`.

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
