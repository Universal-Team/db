FROM python:3.9 AS compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY /source/requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

# Recreate the python symlink since python:3.9 puts it in
# a different location than devkitpro/devkitarm
RUN rm /opt/venv/bin/python && \
    ln -s /usr/bin/python /opt/venv/bin/python

FROM devkitpro/devkitarm

MAINTAINER Pk11 <epicpkmn11@outlook.com>

WORKDIR /app
ENV VIRTUAL_ENV "/opt/venv"
ENV PATH="/opt/venv/bin:$PATH"
COPY --from=compiler /opt/venv /opt/venv
