# For debugging:
# pipenv run gunicorn --version
# pipenv run gunicorn -c gunicorn.conf.py --check-config server:app
# pipenv run gunicorn -c gunicorn.conf.py --print-config server:app
# pipenv run gunicorn -c gunicorn.conf.py --loglevel="debug" server:app

import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
reload = False
max_requests = 1000
user = "root"

# Do **NOT** daemon-ize when using within a Docker image. Otherwise, it'll
# immediately exit with a status code of 0 & no output.
# daemon = True

pythonpath = "/home/code/src"
chdir = "/home/code/src"
