# Deploy Guide — World Leds Go Backend

## Paso 1: Preparar repositorio Git local

Desde la carpeta `wlg_backend`:

### En Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1

# Configurar git (local)
git config user.email "germanrvera@gmail.com"
git config user.name "German Rivera"

# Agregar archivos
git add .

# Primer commit
git commit -m "Initial commit: Django backend with DRF API

- Created Django project structure
- Implemented FamiliaProducto and Proyecto models
- Set up Django REST Framework
- Configured Django Admin
- Added WhiteNoise for statics

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"
```

### En Linux/Mac:
```bash
source venv/bin/activate
chmod +x init_git.sh
./init_git.sh
```

---

## Paso 2: Crear repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre: `wlg-backend` (o lo que prefieras)
3. Descripción: "World Leds Go — Backend API with Django"
4. Elige: **Public** (para que Railway/Render pueda conectarse)
5. No inicialices con README (ya lo tenemos)
6. Click "Create repository"

---

## Paso 3: Conectar repositorio local con GitHub

Copia los comandos que GitHub te muestra:

```bash
git remote add origin https://github.com/YOUR_USERNAME/wlg-backend.git
git branch -M main
git push -u origin main
```

Verifica en GitHub que el código está ahí.

---

## Paso 4: Deploy en Railway ✨

### 1. Crear cuenta en Railway
- https://railway.app
- Puedes usar GitHub para loguear

### 2. Crear nuevo proyecto
- Click "Create New Project"
- Selecciona "Deploy from GitHub"
- Conecta tu cuenta de GitHub
- Selecciona el repositorio `wlg-backend`
- Click "Deploy"

Railway detectará automáticamente que es un proyecto Django.

### 3. Configurar variables de entorno
En Railway, ve a "Variables":

```
SECRET_KEY = (genera una nueva con: python -c "import secrets; print(secrets.token_urlsafe(50))")
DEBUG = False
ALLOWED_HOSTS = your-app.railway.app
DATABASE_URL = (Railway lo proporciona automáticamente)
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 4. Database
Railway puede proporcionar PostgreSQL automáticamente:
- Click "Add Database"
- Selecciona PostgreSQL
- Se agregará automáticamente la variable `DATABASE_URL`

### 5. Ejecutar migraciones
En Railway, en la pestaña "Deployments":
- Click en el deployment activo
- Click "View Logs"
- Las migraciones deberían ejecutarse automáticamente (por el `Procfile`)

### 6. Crear superusuario
En el shell de Railway (o después de deployar):
```bash
python manage.py createsuperuser
```

---

## Alternativa: Deploy en Render

### 1. Crear cuenta en Render
- https://render.com
- Conecta GitHub

### 2. Crear Web Service
- Click "New +"
- "Web Service"
- Conecta tu repositorio `wlg-backend`
- **Build Command:** `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
- **Start Command:** `gunicorn wlg_backend.wsgi`

### 3. Configurar variables de entorno
```
SECRET_KEY = (genera una nueva)
DEBUG = False
DATABASE_URL = (Render lo proporciona)
ALLOWED_HOSTS = your-app.onrender.com
```

### 4. PostgreSQL
- Crea un PostgreSQL service en Render
- Conecta el Web Service a la base de datos

---

## Verificar que funciona

Una vez deployado, tu API estará en:

```
https://your-app.railway.app/api/familias/
https://your-app.railway.app/api/proyectos/
https://your-app.railway.app/admin/
```

### Test con curl:
```bash
curl https://your-app.railway.app/api/familias/
curl https://your-app.railway.app/api/proyectos/
```

---

## Domain personalizado (wlgled.com.ar)

Después de que el app esté corriendo:

### En Railway:
1. Ve a Settings → Domains
2. Agrega tu dominio
3. Railway te dará instrucciones DNS
4. Actualiza DNS en tu registrador

### En Render:
1. Ve a Settings → Custom Domains
2. Agrega tu dominio
3. Sigue las instrucciones DNS

---

## Próximos pasos

Una vez el backend esté online:

1. Actualiza los `fetch()` en los HTML del frontend para apuntar a tu URL de producción
2. Sube el frontend a la misma aplicación (WhiteNoise servirá los estáticos)
3. Conecta el dominio `wlgled.com.ar`

---

## Troubleshooting

### El deploy falla
- Revisa los logs en Railway/Render
- Verifica que `requirements.txt` está actualizado
- Verifica que `Procfile` está correcto

### La base de datos no se migra
- Revisa los logs de "Release" en Railway/Render
- Asegúrate de que `DATABASE_URL` está configurada

### Errores de static files
- Render necesita `python manage.py collectstatic`
- Railway lo ejecuta automáticamente

### Admin panel no carga
- Ejecuta `python manage.py collectstatic` localmente
- Los CSS del admin se sirven desde Django
- WhiteNoise los sirve en producción

---

## Comandos útiles

```bash
# Ver logs en Railway
railway logs

# Ejecutar shell remoto
railway shell

# Ejecutar comando remoto
railway run python manage.py createsuperuser

# Conectar a base de datos PostgreSQL
psql $DATABASE_URL
```

Para Render, usa el panel web o `render logs`.
