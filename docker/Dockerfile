# FROM python:3.7-alpine as build

# # Working directory where all the setup would take place in the image
# WORKDIR /docker-basics

# # # The default user that should be used
# # USER root

# # Create a group and user
# RUN addgroup -S appgroup && adduser -S -h "$(pwd)" appuser -G appgroup

# # The default user that should be used

# # copy the Pipfile & pipfile.lock which contains dependencies to be installed
# COPY ./Pipfile /docker-basics
# COPY ./Pipfile.lock /docker-basics

# # Install Alpine packages needed for the provisioning of the instance with python
# # and other packages
# RUN pip install --upgrade pip
# RUN pip install pipenv
# RUN apk -U update
# RUN apk add --no-cache --update build-base
# RUN apk add libpq


# RUN apk add --no-cache --update --virtual=deps bash zlib-dev zlib bzip2-dev libffi libffi-dev gcc python3-dev musl-dev postgresql-dev libevent-dev gfortran py-pip build-base git && \
#     export LC_ALL=C.UTF-8 && \
#     export LANG=C.UTF-8

# RUN pipenv install

# # Tell docker that all future commands should run as the appuser user

# RUN chown -R appuser:appgroup /root
# RUN chmod 755 /root

# USER appuser
# # RUN export PATH="/root/docker-basics/start_api.sh:$PATH"
# # && \
# #  export PATH="/root/.pyenv /versions/3.6.5:$PATH"
# RUN ls -ahl /root

# RUN rm -rf .cache

# COPY . .

# # Expose the PORT that app would be accessible on
# # EXPOSE 8000

# #  add the port to the docker environment
# # ENV PORT=8000

# CMD ["/bin/bash", "-c", "/docker-basics/docker/start_api.sh"]


FROM python:3.7.7-slim as build

# Working directory where all the setup would take place in the image
WORKDIR /multi-k8

# Install packages needed for the provisioning of the instance with python
# and other packages

RUN pip install --upgrade pip

COPY ./Pipfile /multi-k8
COPY ./Pipfile.lock /multi-k8

RUN pip install --user pipenv
RUN python3 -m pipenv install

FROM python:3.7.7-slim as app

# Working directory where all the setup would take place in the image
WORKDIR /multi-k8

# The default user that should be used
ARG USER_ID=1000
ARG GROUP_ID=1000

ARG APP_USER=appuser

# Create user and group
RUN groupadd -g ${GROUP_ID} ${APP_USER} && useradd -u ${USER_ID} -g ${APP_USER} -s /bin/sh ${APP_USER}

# Install ca certificates
RUN apt-get update \
&& apt-get install ca-certificates -y \
&& apt-get clean

COPY --from=build /root/ /root/
RUN chown -R ${APP_USER}:${APP_USER} /root
RUN chmod 755 /root

COPY . .
# COPY --chown=${APP_USER}:${APP_USER} . .

RUN chown -R ${APP_USER}:${APP_USER} /multi-k8
RUN chmod 755 /multi-k8

# Sert the default user
USER ${APP_USER}

RUN mkdir -p app/static

CMD ["/bin/bash", "-c", "/multi-k8/docker/start_api.sh"]
