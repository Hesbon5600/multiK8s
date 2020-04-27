FROM python:3.7-alpine as build

# Working directory where all the setup would take place in the image
WORKDIR /docker-basics

# # The default user that should be used
# USER root

# Create a group and user
RUN addgroup -S appgroup && adduser -S -h "$(pwd)" appuser -G appgroup

# The default user that should be used

# copy the Pipfile & pipfile.lock which contains dependencies to be installed
COPY ./Pipfile /docker-basics
COPY ./Pipfile.lock /docker-basics

# Install Alpine packages needed for the provisioning of the instance with python
# and other packages
RUN pip install --upgrade pip
RUN pip install pipenv
RUN apk -U update
RUN apk add --no-cache --update build-base
RUN apk add libpq


RUN apk add --no-cache --update --virtual=deps bash zlib-dev zlib bzip2-dev libffi libffi-dev gcc python3-dev musl-dev postgresql-dev libevent-dev gfortran py-pip build-base git && \
    export LC_ALL=C.UTF-8 && \
    export LANG=C.UTF-8

RUN pipenv install

# Tell docker that all future commands should run as the appuser user

RUN chown -R appuser:appgroup /root
RUN chmod 755 /root

USER appuser
# RUN export PATH="/root/docker-basics/start_api.sh:$PATH"
# && \
#  export PATH="/root/.pyenv /versions/3.6.5:$PATH"
RUN ls -ahl /root

RUN rm -rf .cache

COPY . .

# Expose the PORT that app would be accessible on
# EXPOSE 8000

#  add the port to the docker environment
# ENV PORT=8000

CMD ["/bin/bash", "-c", "/docker-basics/docker/start_api.sh"]