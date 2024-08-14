echo "Building project packages..."
python3 -m pip install -r requirements.txt

echo "Building Tailwind CSS..."
NODE_ENV=production python3 manage.py tailwind build

python3 manage.py migrate --noinput
python3 manage.py makemigrations --noinput

python3 manage.py collectstatic --noinput
