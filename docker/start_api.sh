#!/bin/bash
# find ~/ -name docker-basics\*
# sleep 10
# ls -a
source /root/.local/share/virtualenvs/docker-basics-*/bin/activate
# export $(grep -v '^#' .env | xargs)

# pipenv shell
echo "<<<<<<<<<< Export LANG to the Env>>>>>>>>>>"

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

sleep 3
echo "<<<<<<<< Database Setup and Migrations Starts >>>>>>>>>"
# Run database migrations
python manage.py migrate


sleep 5
echo "<<<<<<< Database Setup and Migrations Complete >>>>>>>>>>"
echo " "


# echo "<<<<<<< Remove any pending celery tasks >>>>>>>>>>"
# echo " "


# celery purge -f

# sleep 5
echo " "
echo "<<<<<<<<<<<<<<<<<<<< START Celery >>>>>>>>>>>>>>>>>>>>>>>>"

# start Celery worker
 celery -A app worker -l info --pool=gevent --concurrency=500 &

# # start celery beat
# celery -A celery_conf.celery_periodic_scheduler beat --loglevel=info &

sleep 5
echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
# python manage.py runserver 0.0.0.0:8000
# Start the API with gunicorn
gunicorn --bind 0.0.0.0:8000 app.wsgi --reload --access-logfile '-' --workers 2
