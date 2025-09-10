# ====
# Base
# ====
FROM python:3.13-slim AS base

ENV PATH=/home/code/venv/bin:$PATH:.
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/home/code/src

ENV OS_DEPENDENCIES="curl"

RUN apt-get update && \
    apt-get install --no-install-recommends -y ${OS_DEPENDENCIES} \
    && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip uv

RUN mkdir -p /home/code/src

RUN useradd django --group=staff --create-home --shell /bin/bash && \
    chown -R django:staff /home/code

USER django

RUN python -m uv venv /home/code/venv

WORKDIR /home/code

COPY --chown=django:staff pyproject.toml /home/code/pyproject.toml
COPY --chown=django:staff uv.lock /home/code/uv.lock

# Since this image gets re-used for other things, install *only* the main
# dependencies.
RUN uv sync --no-dev

# For this stage, for best re-use, we copy over the code instead of mounting it
# w/ a volume.
COPY --chown=django:staff ./src/ /home/code/src/

# In case anyone needs to be able to just run a plain base image for debugging,
# make the container spin infinitely so shelling in is possible.
CMD [ "tail", "-f", "/dev/null" ]


# ===========
# Development
# ===========
FROM base AS dev

# Extra development conveniences can be installed here. Examples are `git`,
# `vim`, `postgresql-client`, etc. Anything to make working within the
# containers nicer from a developer's standpoint.
ENV OS_DEPENDENCIES="curl git vim postgresql-client"

USER root

# We *don't* kill the Apt caches here. Because that's a PITA when you're
# developing, then shell in, then have to always run `apt-get update` before
# installing/testing anything else.
RUN apt-get update && \
    apt-get install --no-install-recommends -y ${OS_DEPENDENCIES}

USER django

COPY --chown=django:staff pyproject.toml /home/code/pyproject.toml
COPY --chown=django:staff uv.lock /home/code/uv.lock

# Since we're building off the already-constructed base image, all we need are
# the extra development dependencies.
RUN uv sync

# It's not explicitly here, but we're also going to live-mount the user's
# `/src` directory into `/home/code/src` as a Docker Volume, so that their
# changes automatically show up in the running container(s).

EXPOSE 8000

CMD [ "uv", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000" ]


# ==========
# Production
# ==========

# We rebuild from scratch here, so that we don't pick up anything "extra" that
# was installed into the `dev` image, and so that the production image is as
# small/clean as possible.
FROM python:3.13-slim AS prod

ENV PATH=/home/code/venv/bin:$PATH:.
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/home/code/src

ENV OS_DEPENDENCIES="curl"

# Kill the Apt caches at the end of the OS installs, for the smallest possible
# production image.
RUN apt-get update && \
    apt-get install --no-install-recommends -y ${OS_DEPENDENCIES} \
    && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip uv

RUN mkdir -p /home/code/src && \
    mkdir -p /home/code/static && \
    mkdir -p /home/code/tmp

RUN useradd django --group=staff --create-home --shell /bin/bash && \
    chown -R django:staff /home/code

USER django

RUN python -m uv venv /home/code/venv

WORKDIR /home/code

# Copy over the pre-built dependencies, for fastest build times.
COPY --from=base --chown=django:staff /home/code/venv /home/code/venv
COPY --from=base --chown=django:staff /home/code/pyproject.toml /home/code/pyproject.toml
COPY --from=base --chown=django:staff /home/code/uv.lock /home/code/uv.lock

# Here, we're pulling in the production gunicorn config.
COPY --chown=django:staff ./docker/gunicorn.conf.py /home/code/gunicorn.conf.py
COPY --chown=django:staff ./src/ /home/code/src/

COPY --chown=django:staff ./frontend/dist/ /home/code/static/

EXPOSE 8000

# Go, little image, go!
CMD [ "uv", "run", "gunicorn", "--worker-tmp-dir", "/home/code/tmp", "-c", "gunicorn.conf.py", "config.wsgi:application" ]
