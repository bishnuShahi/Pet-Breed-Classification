# Install Python dependencies
echo "Installing dependencies...."
pip install -r requirements.txt

# Run database migrations
echo "Migrating database...."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run any other commands
echo "Build complete!"