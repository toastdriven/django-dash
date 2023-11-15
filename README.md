# djangodash

The code that powers the [Django Dash](https://django-dash.com/).


## Quick Start

```bash
$ git clone ...
$ cd djangodash
$ just setup

# Put your code in the `src/` directory.
# The Docker/Gunicorn setup expects a `src/config/wsgi.py` to be present.
```


## Requirements

Mostly, just have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed, as well as [Just](https://just.systems/) for nice conveniences.


## Setup

```
$ just run
```

...or...

```bash
$ docker compose build
$ docker compose run --rm web bash -c "pipenv run python src/manage.py migrate"
$ docker compose up
```

Then visit http://localhost:8000/ in your web browser.


## More To Come

TBD


## License

New BSD
