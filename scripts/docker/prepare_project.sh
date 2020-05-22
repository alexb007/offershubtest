#!/usr/bin/env bash

until cd /apps/offershubtest/
do
    echo "Waiting for django volume..."
done

echo "Running migration..."
python manage.py migrate --noinput
