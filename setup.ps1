# Setup script for World Leds Go Backend

Write-Host "=== World Leds Go Backend Setup ===" -ForegroundColor Green

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv
if ($?) {
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate venv
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
if ($?) {
    Write-Host "✓ Virtual environment activated" -ForegroundColor Green
}

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($?) {
    Write-Host "✓ Dependencies installed" -ForegroundColor Green
}

# Run migrations
Write-Host "Running migrations..." -ForegroundColor Yellow
python manage.py migrate
if ($?) {
    Write-Host "✓ Migrations completed" -ForegroundColor Green
}

# Create superuser (optional)
Write-Host ""
Write-Host "Creating superuser..." -ForegroundColor Yellow
Write-Host "When prompted, enter:"
Write-Host "  Username: admin"
Write-Host "  Email: admin@wlgled.com"
Write-Host "  Password: admin123 (or your preferred password)"
Write-Host ""
python manage.py createsuperuser --username admin --email admin@wlgled.com --noinput
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.get(username='admin'); u.set_password('admin123'); u.save()"
Write-Host "✓ Superuser created" -ForegroundColor Green

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Green
Write-Host ""
Write-Host "To start the development server, run:" -ForegroundColor Cyan
Write-Host "  .\venv\Scripts\Activate.ps1"
Write-Host "  python manage.py runserver"
