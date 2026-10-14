#!/bin/bash
set -e

echo "Starting World Leds Go backend..."

echo "1. Running migrations..."
python manage.py migrate --noinput

echo "2. Loading initial data..."
python manage.py load_initial_data

echo "3. Creating admin user..."
python manage.py create_admin

echo "4. Collecting static files..."
python manage.py collectstatic --noinput

echo "5. Starting gunicorn..."
gunicorn wlg_backend.wsgi:application --bind 0.0.0.0:$PORT
