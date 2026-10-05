#!/bin/bash

# Initialize Git repository and make first commit

echo "=== Initializing Git Repository ==="

# Configure git (local only)
git config user.email "germanrvera@gmail.com"
git config user.name "German Rivera"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Django backend with DRF API

- Created Django project structure with settings (dev/prod)
- Implemented FamiliaProducto and Proyecto models
- Set up Django REST Framework viewsets and serializers
- Configured Django Admin with custom admin classes
- Added WhiteNoise for static file serving
- Included management command to load initial data
- Added setup scripts and documentation

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"

echo ""
echo "✓ Git repository initialized and first commit created"
echo ""
echo "Next steps:"
echo "1. Create repository on GitHub (https://github.com/new)"
echo "2. Run: git remote add origin https://github.com/YOUR_USERNAME/wlg-backend.git"
echo "3. Run: git branch -M main"
echo "4. Run: git push -u origin main"
