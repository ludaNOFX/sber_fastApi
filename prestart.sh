#!/bin/sh
#chmod +x ./run.sh
export PYTHONPATH=$PYTHONPATH:./app

# Let the DB start
#python ./app/backend_prestart.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python ./app/initial_data.py