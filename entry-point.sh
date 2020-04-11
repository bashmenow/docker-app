#!/bin/bash
set -e
if [ "$ENV" = 'DEV' ]; then
 echo "Running Development Server"
 exec python "main.py"
elif [ "$ENV" = 'UNIT' ]; then
 echo "Running Unit Tests"
 exec python "tests.py"
elif [ "$ENV" = 'PROD' ]; then
 echo "Running Production Server"
 exec gunicorn --bind 0.0.0.0:9090 main.py:app
fi
