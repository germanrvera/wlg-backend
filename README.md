# World Leds Go — Backend API

Django REST Framework API para el catálogo de productos y proyectos de World Leds Go.

## Instalación

### 1. Clonar o descargar el proyecto
```bash
cd wlg_backend
```

### 2. Crear un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus valores
```

### 5. Crear la base de datos
```bash
python manage.py migrate
```

### 6. Crear superusuario (para Django Admin)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```

El servidor estará disponible en `http://localhost:8000`

## Endpoints de API

### Familias de Productos
- **GET** `/api/familias/` — Lista todas las familias activas
- **GET** `/api/familias/<slug>/` — Detalle de una familia
- **GET** `/api/familias/?search=query` — Buscar familias

### Proyectos
- **GET** `/api/proyectos/` — Lista todos los proyectos activos
- **GET** `/api/proyectos/<slug>/` — Detalle de un proyecto
- **GET** `/api/proyectos/?search=query` — Buscar proyectos

## Django Admin

Acceder a `http://localhost:8000/admin` con el superusuario.

Aquí puedes:
- Crear, editar y eliminar familias de productos
- Crear, editar y eliminar proyectos
- Cambiar estado (activo/inactivo)
- Cargar imágenes

## Estructura

```
wlg_backend/
├── manage.py
├── requirements.txt
├── .env.example
├── wlg_backend/
│   ├── settings/
│   │   ├── base.py       (configuración compartida)
│   │   ├── dev.py        (desarrollo)
│   │   └── prod.py       (producción)
│   ├── urls.py
│   └── wsgi.py
├── catalogo/             (app principal)
│   ├── models.py         (FamiliaProducto, Proyecto)
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
└── static/               (archivos HTML del sitio - servidos por WhiteNoise)
```

## Deploy

### Railway
1. Crear proyecto en Railway
2. Conectar repositorio Git
3. Variables de entorno en Railway
4. Deploy automático

### Render
1. Crear Web Service en Render
2. Conectar repositorio
3. Build command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
4. Start command: `gunicorn wlg_backend.wsgi`
5. Variables de entorno

## Tecnologías

- Django 4.2
- Django REST Framework 3.14
- WhiteNoise (servir estáticos)
- Gunicorn (WSGI server)
- PostgreSQL (producción)
