echo "Building project packages..."
python3 -m pip install -r requirements.txt

echo "Building Tailwind CSS..."
NODE_ENV=production python3 manage.py tailwind build
