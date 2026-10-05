#!/bin/bash

echo "=== World Leds Go Backend Setup ==="

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
echo "✓ Virtual environment created"

# Activate venv
source venv/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Run migrations
echo "Running migrations..."
python manage.py migrate
echo "✓ Migrations completed"

# Create superuser
echo ""
echo "Creating superuser (admin/admin123)..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@wlgled.com', 'admin123')
    print("✓ Superuser created")
else:
    print("✓ Superuser already exists")
EOF

echo ""
echo "=== Setup Complete ==="
echo ""
echo "To start the development server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
