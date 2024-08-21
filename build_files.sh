python3.12 pip install -U pip

# Install dependencies
python3.12 -m pip install -r requirements.txt

# Make migrations
python3.12 manage.py makemigrations --noinput
python3.12 manage.py migrate --noinput

python3.12 manage.py collectstatic --noinput --clear