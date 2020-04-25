#!/bin/bash
# find ~/ -name virtualenvs\*
export PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
export PATH="$PATH:$PYTHON_BIN_PATH"
# pipenv install
# pipenv run python manage.py runserver
alias test='coverage run --source=app manage.py test --verbosity=2  && coverage report -m'
alias runserver='python manage.py runserver'
alias notebook='python manage.py shell_plus --notebook'
alias migrate='python manage.py migrate'
alias makemigrations='python manage.py makemigrations'

# export $(grep -v '^#' .env | xargs)