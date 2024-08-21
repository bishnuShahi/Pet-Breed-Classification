python3.12 pip install -U pip

# Install dependencies
python3.12 -m pip install -r requirements.txt

# Make migrations
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput
#Install whitenoise
python3.12 manage.py whitenoise

python3.12 manage.py collectstatic --noinput --clear