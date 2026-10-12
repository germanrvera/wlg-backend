# Arquitectura — World Leds Go

## Stack

| Capa | Tecnología | Hosting |
|---|---|---|
| Frontend (HTML) | HTML + CSS + JS inline | Vercel |
| Backend (API) | Django 5.0.1 + DRF | Render |
| Base de datos | PostgreSQL | Render |
| Media (imágenes) | Cloudflare R2 | Cloudflare |
| DNS / CDN | Cloudflare | Cloudflare |

Sin bundler, sin framework frontend. Todo el CSS y JS va inline en cada template.

---

## Flujo de datos

```
Usuario
  └── wlg-frontend.vercel.app (HTML estático)
        └── fetch() → wlg-backend.onrender.com/api/
              └── Django + DRF
                    └── PostgreSQL (datos)
                    └── Cloudflare R2 (imágenes)
```

El HTML se sirve desde Vercel. Las llamadas a la API van al backend en Render. Las imágenes subidas desde el admin de Django se almacenan en R2 y se sirven desde su URL pública.

---

## Repositorio

```
wlg_backend/
├── vercel.json              ← configuración de Vercel (rutas)
├── ARQUITECTURA.md
├── SESION_CAMBIOS.md
├── requirements.txt
├── manage.py
├── .env.example
│
├── wlg_backend/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py          ← R2 storage configurado aquí
│   ├── urls.py
│   └── wsgi.py
│
├── catalogo/
│   ├── models.py            ← modelos de datos
│   ├── serializers.py       ← serialización para la API
│   ├── views.py             ← viewsets
│   ├── urls.py              ← rutas de la API
│   ├── admin.py             ← panel de administración
│   └── migrations/
│
└── templates/               ← todos los HTML del sitio
    ├── vercel.json          ← rewrites de rutas para Vercel
    ├── home.html            → /
    ├── familias.html        → /familias
    ├── familia.html         → /familia/<slug>
    ├── proyectos.html       → /proyectos
    ├── proyecto.html        → /proyecto/<slug>
    ├── recursos.html        → /recursos
    ├── novedades.html       → /novedades
    ├── experiencia.html     → /experiencia
    ├── contactar.html       → /contacto
    └── historia.html        → /historia
```

---

## API endpoints

| Método | URL | Descripción |
|---|---|---|
| GET | `/api/familias/` | Lista todas las familias activas |
| GET | `/api/familias/<slug>/` | Detalle de una familia |
| GET | `/api/proyectos/` | Lista todos los proyectos activos |
| GET | `/api/proyectos/<slug>/` | Detalle de un proyecto |
| GET | `/api/hero-slides/` | Slides del hero del home |
| GET | `/api/lanzamientos/` | Cards de lanzamiento para el carrusel |
| GET | `/api/distribuidores/` | Lista de distribuidores |
| GET | `/api/recursos/` | Recursos descargables |
| POST | `/api/solicitudes-distribuidor/` | Solo en PythonAnywhere — no tocar |

> `WLG_API_BASE = 'https://germanrvera.pythonanywhere.com'` es el CPQ de distribuidores. No cambiar esta URL en ningún HTML.

---

## Modelos de datos

### FamiliaProducto
Familia de productos (Galuy, Cetus, Petra, etc.)
- `nombre`, `slug`, `descripcion`, `tipo`, `macro`, `orden`, `activo`
- `imagen` (R2) o `photo` (URL externa — tiene prioridad)
- Filtros técnicos en JSONField: `filter_ct`, `filter_ip`, `filter_dim_sys`, etc.

### Producto
Ítem individual dentro de una familia.
- `familia` (FK), `codigo`, `descripcion`, `imagen`, `orden`, `activo`

### Proyecto
Proyecto de portfolio.
- `nombre`, `slug`, `ubicacion`, `año`, `tipo_espacio`
- `imagen_principal` (R2)
- `galeria` (JSON: lista de URLs)
- `bloques` (JSON: narrativa del proyecto)
- `ficha_tecnica` (JSON: especificaciones)

### HeroSlide
Slides del hero del home. Controlados desde el admin.

### Lanzamiento
Cards del carrusel de lanzamientos en el home.
- Vincula a una `FamiliaProducto` o un `Producto` (uno de los dos)
- `titulo` y `subtitulo` opcionales (si vacíos, toma el nombre del registro vinculado)
- `imagen` (R2) o `photo` (URL externa)

### Distribuidor
Lista de distribuidores para el localizador en `/contacto`.

### RecursoDescargable
Fichas técnicas, IES, CAD para `/recursos`.

### Configuracion
Pares clave-valor por página para texto editable desde el admin.

---

## Variables de entorno (Render)

```
SECRET_KEY=...
DEBUG=False
DATABASE_URL=...
R2_ACCESS_KEY_ID=...
R2_SECRET_ACCESS_KEY=...
R2_BUCKET_NAME=wlg-media
R2_ACCOUNT_ID=...
R2_PUBLIC_URL=https://...
```

En desarrollo sin R2 configurado, las imágenes se guardan en disco local.

---

## Deploy

El repo `wlg-backend` en GitHub está conectado a **dos servicios**:

| Push a `main` | Qué pasa |
|---|---|
| Render | Redeploya Django (API) automáticamente |
| Vercel | Redeploya los HTML estáticos automáticamente |

No hay pasos manuales. El ciclo es: editar archivos → `git add` → `git commit` → `git push origin main`.

---

## Agregar una página nueva

1. Crear el HTML en `templates/nueva-pagina.html`
2. Agregar la ruta en `wlg_backend/urls.py` (Django)
3. Agregar el rewrite en `templates/vercel.json`:
   ```json
   { "source": "/nueva-pagina", "destination": "/nueva-pagina.html" }
   ```
4. Agregar el link en el nav de todos los templates si corresponde
5. Push

---

## Agregar un producto o familia

1. Entrar al admin de Django: `wlg-backend.onrender.com/admin`
2. Familia: completar nombre, slug, tipo, imagen (va a R2 automáticamente), filtros técnicos
3. Producto: asociar a la familia, cargar código y descripción
4. Activar el registro (`activo = True`)
5. La API lo expone automáticamente — no hay deploy necesario

---

## Diseño — reglas fijas

**Colores**

| Variable | Valor | Uso |
|---|---|---|
| `--bg` | `#080808` | Fondo general |
| `--gold` | `#c9a96e` | Acento primario |
| `--white` | `#ede9e2` | Texto principal |
| `--dim` | `rgba(237,233,226,.45)` | Texto secundario |
| `--dim2` | `rgba(237,233,226,.18)` | Bordes |
| `--gray2` | `#b3aea5` | Texto terciario |
| `--panel` | `rgba(10,9,7,.9)` | Fondos de paneles |

**Tipografía:** Urbanist 200/300/400/500 (Google Fonts)

**Botones:** corte diagonal en esquina superior derecha
```css
clip-path: polygon(0 0, calc(100% - 11px) 0, 100% 11px, 100% 100%, 0 100%);
```

**Nav desktop** (orden canónico):
```
Productos → Proyectos → Novedades → Laboratorio → Recursos → Powergear
```
- `Productos` abre mega-menu con `onmouseenter="openMega('megaProductos')"`
- Los demás cierran con `onmouseenter="closeMega()"`
- Powergear va también en el menú mobile
- Powergear nunca tiene `class="active"`

**Prohibido:**
- `--terra` (color eliminado)
- `cursor: none` en cualquier selector
- `.cursor-dot`, `.cursor-ring` (sistema eliminado)
- Powergear en el nav desktop sin `onmouseenter="closeMega()"`

---

## Librerías externas

| Librería | Versión | Dónde |
|---|---|---|
| GSAP + ScrollTrigger | 3.x | Páginas principales |
| Three.js | r128 | Solo `experiencia.html` |
| Google Fonts (Urbanist) | — | Todas las páginas |
| Cormorant Garamond | — | Títulos serif |

Todas se cargan desde CDN. No hay `node_modules` ni bundler.
