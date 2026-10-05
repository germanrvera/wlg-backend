# Deploy en Render (GRATUITO)

## ✅ Por qué Render

- **Gratuito** — Free Tier incluido
- **Deploy fácil** — Desde GitHub en 1 click
- **PostgreSQL incluido** — BD relacional gratuita
- **HTTPS automático** — SSL gratis
- **Escalable** — Upgrade fácil si crece

---

## Paso 1: Subir código a GitHub

Desde la carpeta `wlg_backend`:

```bash
git config user.email "germanrvera@gmail.com"
git config user.name "German Rivera"
git add .
git commit -m "Initial commit: Django backend API"
git remote add origin https://github.com/YOUR_USERNAME/wlg-backend.git
git branch -M main
git push -u origin main
```

Verifica que el código está en GitHub.

---

## Paso 2: Crear cuenta en Render

1. Ve a https://render.com
2. Click **"Sign up"**
3. Usa GitHub para signup rápido
4. Autoriza Render a acceder tu GitHub

---

## Paso 3: Crear Web Service

1. En dashboard, click **"New +"** (arriba a la derecha)
2. Selecciona **"Web Service"**
3. **"Connect a repository"** → Selecciona `wlg-backend`
4. Llena los datos:

   | Campo | Valor |
   |---|---|
   | Name | `wlg-backend` |
   | Environment | `Python 3` |
   | Build Command | `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput` |
   | Start Command | `gunicorn wlg_backend.wsgi` |
   | Plan | `Free` |

5. Click **"Create Web Service"**

Render inicia el deploy automáticamente.

---

## Paso 4: Crear PostgreSQL Database

1. Click **"New +"** → **"PostgreSQL"**
2. Llena:

   | Campo | Valor |
   |---|---|
   | Name | `wlg-db` |
   | Database | `wlg_db` |
   | User | `wlg_user` |
   | Region | Igual a tu Web Service |
   | Plan | `Free` |

3. Click **"Create Database"**

Render crea la BD automáticamente.

---

## Paso 5: Conectar Database al Web Service

1. Ve al Web Service que creaste
2. Click **"Environment"**
3. Agrega variable (Render debería hacerlo automático):

   ```
   DATABASE_URL = (Render lo proporciona automáticamente de PostgreSQL)
   ```

   Si no aparece automático, ve a la BD PostgreSQL:
   - Click en la BD
   - Copia la URL de conexión
   - En Web Service → Environment → Agrega:
     ```
     DATABASE_URL = postgres://usuario:password@host:puerto/dbname
     ```

---

## Paso 6: Configurar variables de entorno

En tu Web Service, click **"Environment"** y agrega:

```
SECRET_KEY = (genera con: python -c "import secrets; print(secrets.token_urlsafe(50))")
DEBUG = False
ALLOWED_HOSTS = tu-app.onrender.com
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## Paso 7: Esperar deploy

1. Click **"Deployments"** para ver el progreso
2. Espera a que esté **"Live"** (verde)
3. Verás logs del build

Si hay error, revisa los logs y corrige.

---

## Paso 8: Crear superusuario

Una vez deployado, ve a **"Shell"** en Render:

```bash
python manage.py createsuperuser --username admin --email admin@wlgled.com
# Ingresa contraseña: admin123
```

---

## ✅ ¡Listo!

Tu API está en:
```
https://tu-app.onrender.com/api/familias/
https://tu-app.onrender.com/api/proyectos/
https://tu-app.onrender.com/admin/
```

Prueba:
```bash
curl https://tu-app.onrender.com/api/familias/
```

---

## Cargar datos iniciales

En el Shell de Render:

```bash
python manage.py load_initial_data
```

---

## Limitaciones del Free Tier

- Se duerme después de **15 minutos sin requests**
- **0.5 GB RAM**
- **10 GB almacenamiento en BD**
- PostgreSQL gratuito con límites

**Solución:** Si crece, upgrade a plan pago ($7/mes).

---

## URLs de tu app

- **API Familias:** `https://tu-app.onrender.com/api/familias/`
- **API Proyectos:** `https://tu-app.onrender.com/api/proyectos/`
- **Admin Django:** `https://tu-app.onrender.com/admin/`

---

## Actualizar código

Si haces cambios:

```bash
# Local
git add .
git commit -m "Update..."
git push origin main

# Render lo detecta automáticamente y redeploy
# Verifica en "Deployments"
```

---

## Agregar dominio personalizado

1. En Web Service, click **"Settings"**
2. Scroll a **"Custom Domains"**
3. Agrega `wlgled.com.ar`
4. Render te da instrucciones DNS
5. Configura DNS en tu registrador

---

## Troubleshooting

### El build falla
- Revisa logs en "Deployments"
- Verifica `requirements.txt`
- Asegúrate de que `Procfile` está bien (Render usa Build/Start commands)

### Database error
- Verifica que `DATABASE_URL` está en Environment
- Comprueba que la BD está corriendo
- Intenta `python manage.py migrate` en Shell

### Admin CSS no carga
- Ejecuta en Shell: `python manage.py collectstatic --noinput`
- Reload del app

### "Internal Server Error" (500)
- Revisa logs: **"Logs"** en Web Service
- Verifica variables de entorno
- Asegúrate que SECRET_KEY está configurada

---

## Ventajas de Render vs PythonAnywhere

| Aspecto | Render | PythonAnywhere |
|---|---|---|
| Costo | ✅ Gratuito | ✅ Gratuito |
| BD | ✅ PostgreSQL | MySQL |
| Setup | ✅ Automático | Más manual |
| Performance | ✅ Bueno | Bueno |
| Se duerme | ⚠️ Sí (15 min) | No |

---

## Próximos pasos

1. ✅ Backend corriendo en Render
2. 🌐 Conectar frontend HTML (fetch al API)
3. 🎯 Dominio personalizado

¡Listo para integrar con el frontend!
