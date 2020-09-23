#!/bin/bash
export SCRIPTPATH=$(dirname $(realpath $0))
export PIPENV_PIPFILE=$SCRIPTPATH/Pipfile

# go into the virtual environment's python and run the script
exec pipenv run python $SCRIPTPATH/media_probe.py "$@"
