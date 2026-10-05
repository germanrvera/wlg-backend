# Setup Instructions — World Leds Go Backend

## En Windows (PowerShell)

### 1. Abre PowerShell en la carpeta `wlg_backend`

```powershell
# Navega a la carpeta
cd "C:\Users\germa\OneDrive\Documentos\Claude\Projects\Nueva pagina\wlg_backend"
```

### 2. Ejecuta el script de setup

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

Esto hará:
- Crear virtualenv
- Instalar dependencias
- Ejecutar migrations
- Crear superusuario (admin / admin123)

### 3. Cargar datos iniciales

Después de que el setup termine, ejecuta:

```powershell
.\venv\Scripts\Activate.ps1
python manage.py load_initial_data
```

### 4. Iniciar servidor de desarrollo

```powershell
python manage.py runserver
```

El servidor estará en: http://localhost:8000

---

## En Linux/Mac (Bash)

### 1. Abre terminal en la carpeta `wlg_backend`

```bash
cd "C:\Users\germa\OneDrive\Documentos\Claude\Projects\Nueva pagina\wlg_backend"
```

### 2. Dale permisos de ejecución al script

```bash
chmod +x setup.sh
```

### 3. Ejecuta el script

```bash
./setup.sh
```

### 4. Cargar datos iniciales

```bash
source venv/bin/activate
python manage.py load_initial_data
```

### 5. Iniciar servidor

```bash
python manage.py runserver
```

---

## Verificar que todo funciona

Una vez que el servidor esté corriendo:

1. **API de familias:** http://localhost:8000/api/familias/
2. **API de proyectos:** http://localhost:8000/api/proyectos/
3. **Django Admin:** http://localhost:8000/admin (usuario: admin / contraseña: admin123)

---

## Troubleshooting

### Error: "No module named 'django'"
- Asegúrate de que el virtualenv está activado
- Windows: `.\venv\Scripts\Activate.ps1`
- Linux/Mac: `source venv/bin/activate`

### Error: "db.sqlite3 is locked"
- Cierra otros procesos Django que estén corriendo
- Borra `db.sqlite3` y vuelve a hacer `python manage.py migrate`

### Las migraciones no se aplican
```bash
python manage.py migrate --run-syncdb
```

### Crear nuevo superusuario
```bash
python manage.py createsuperuser
```

---

## Variables de entorno (.env)

Por defecto usa SQLite. Si quieres usar PostgreSQL:

1. Instala PostgreSQL
2. Crea una BD: `createdb wlg_db`
3. Edita `.env`:
   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=wlg_db
   DB_USER=postgres
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_PORT=5432
   ```
4. Instala psycopg2: `pip install psycopg2-binary`
5. Ejecuta migrations: `python manage.py migrate`

---

## Próximos pasos

Una vez que el backend esté corriendo:

1. Conectar los `fetch()` del frontend HTML al API
2. Copiar archivos HTML a `wlg_backend/static/`
3. Configurar WhiteNoise para servir los estáticos
4. Deploy en Railway o Render
