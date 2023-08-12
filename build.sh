#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt
python3.9 -m pip install django
python3.9 -m pip install PyMySQL
python3.9 -m pip install dj-database-url
python3.9 -m pip install django-active-link
python3.9 -m pip install razorpay
echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
