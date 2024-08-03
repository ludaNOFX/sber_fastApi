#!/bin/sh
#chmod +x ./run.sh

#PRE_START_PATH=${PRE_START_PATH:-prestart.sh}
#echo "Checking for script in $PRE_START_PATH"
#if [ -f $PRE_START_PATH ] ; then
#    echo "Running script $PRE_START_PATH"
#    . "$PRE_START_PATH"
#else
#    echo "There is no script $PRE_START_PATH"
#fi

alembic upgrade head

exec uvicorn --reload --host 0.0.0.0 --port 8001 app.main:app