# Deploy en PythonAnywhere (GRATUITO)

## ✅ Por qué PythonAnywhere

- **Gratuito** — Plan Beginner sin pagar
- **Siempre online** — No se duerme
- **Django-ready** — Hecho para Python/Django
- **Fácil setup** — Menos configuración que Railway
- **SSL incluido** — HTTPS gratis

---

## Paso 1: Crear cuenta

1. Ve a https://www.pythonanywhere.com/
2. Click "Sign Up"
3. Usa GitHub para signup rápido
4. Verifica email
5. Acepta el plan Beginner (gratuito)

---

## Paso 2: Subir código a GitHub

Primero, haz commit y push a GitHub (desde carpeta `wlg_backend`):

```bash
git config user.email "germanrvera@gmail.com"
git config user.name "German Rivera"
git add .
git commit -m "Initial Django backend"
git remote add origin https://github.com/YOUR_USERNAME/wlg-backend.git
git branch -M main
git push -u origin main
```

Verifica que el código está en GitHub: `https://github.com/YOUR_USERNAME/wlg-backend`

---

## Paso 3: Crear Web App en PythonAnywhere

1. En el dashboard, click **"Web"** (izquierda)
2. Click **"Add a new web app"**
3. Selecciona:
   - Python version: **3.11**
   - Framework: **Django**
4. PythonAnywhere crea un app Django default

Esto crea carpetas en: `/home/tu_username/mysite/`

---

## Paso 4: Clonar nuestro código

1. Click **"Consoles"** → **"Bash console"**
2. Navega a la carpeta:
   ```bash
   cd /home/tu_username
   ```
3. Elimina el Django default (opcional):
   ```bash
   rm -rf mysite
   ```
4. Clona nuestro repositorio:
   ```bash
   git clone https://github.com/YOUR_USERNAME/wlg-backend.git mysite
   cd mysite
   ```

---

## Paso 5: Crear virtual environment

En la bash console:

```bash
mkvirtualenv --python=/usr/bin/python3.11 mysite
pip install -r requirements.txt
```

---

## Paso 6: Crear base de datos

En bash console:

```bash
python manage.py migrate
```

---

## Paso 7: Crear superusuario

```bash
python manage.py createsuperuser --username admin --email admin@wlgled.com
# Cuando pida contraseña, ingresa: admin123
```

---

## Paso 8: Configurar Web App

1. Vuelve a **"Web"** en el dashboard
2. Click en tu web app
3. En la sección **"Code"**:
   - **Source code:** `/home/tu_username/mysite`
   - **Working directory:** `/home/tu_username/mysite`

4. En **"WSGI configuration file"**:
   - Click en el archivo WSGI
   - Reemplaza el contenido con esto:

```python
import os
import sys

path = '/home/tu_username/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wlg_backend.settings.prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

5. En **"Virtualenv"**:
   - Ingresa: `/home/tu_username/.virtualenvs/mysite`

---

## Paso 9: Configurar variables de entorno

1. Click **"Web"** → Tu app
2. Scroll hasta **"Web app"**
3. Click en el archivo `.env` (o agrégalo manualmente)

Contenido del `.env`:
```
SECRET_KEY=django-insecure-tu-secret-key-aqui
DEBUG=False
ALLOWED_HOSTS=tu_username.pythonanywhere.com
```

Para generar una SECRET_KEY:
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## Paso 10: Reload

1. En la página de Web App
2. Click botón **"Reload"** (verde, arriba)
3. Espera 10 segundos

---

## ✅ ¡Listo!

Tu API está en:
```
https://tu_username.pythonanywhere.com/api/familias/
https://tu_username.pythonanywhere.com/api/proyectos/
https://tu_username.pythonanywhere.com/admin/
```

Prueba en el navegador o con curl:
```bash
curl https://tu_username.pythonanywhere.com/api/familias/
```

---

## Admin Django

Acceder a:
```
https://tu_username.pythonanywhere.com/admin/
```

Login:
- Username: `admin`
- Password: `admin123`

Desde aquí puedes:
- Crear/editar familias de productos
- Crear/editar proyectos
- Cargar imágenes

---

## Limitaciones del plan Beginner

- **100 requests/día** (suficiente para testing)
- **512 MB almacenamiento**
- **MySQL** (no PostgreSQL)
- **Subdomain** PythonAnywhere (sin dominio personalizado)

Si necesitas más, upgradea a **Hacker Plan** ($5/mes) o migra a otra plataforma.

---

## Actualizar código

Si cambias algo localmente:

```bash
# Local
git add .
git commit -m "Update..."
git push origin main

# En PythonAnywhere bash console
cd /home/tu_username/mysite
git pull origin main
python manage.py migrate  # si hay cambios en modelos
python manage.py collectstatic --noinput  # estáticos
# Reload desde Web dashboard
```

---

## Cargar datos iniciales

En PythonAnywhere bash console:

```bash
cd /home/tu_username/mysite
source /home/tu_username/.virtualenvs/mysite/bin/activate
python manage.py load_initial_data
```

---

## Troubleshooting

### Error 500
- Revisa los logs: Click "Web" → "Error log"
- Verifica `.env` y variables
- Comprueba que WSGI está bien configurado

### "Permission denied"
- Verifica que los permisos de carpeta son correctos
- En bash: `chmod -R 755 /home/tu_username/mysite`

### Database errors
- PythonAnywhere usa MySQL por defecto
- Asegúrate de que `python manage.py migrate` se ejecutó

### Static files no cargan
```bash
python manage.py collectstatic --noinput
```

---

## Próximos pasos

1. ✅ Backend corriendo en PythonAnywhere
2. 🌐 Integrar frontend HTML (conectar fetch() al API)
3. 🎯 Conectar dominio personalizado (wlgled.com.ar)

Para dominio personalizado:
- Ve a **"Web"** → Tu app → **"Web address"**
- Click "Add a new web address"
- Ingresa tu dominio
- Sigue instrucciones DNS
