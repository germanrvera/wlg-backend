# Opciones de Deploy Gratuitas/Baratas

## 1. **Render** ⭐ (RECOMENDADO)
- **Costo:** Gratuito con limitaciones
- **Ventajas:** 
  - Fácil deploy desde GitHub
  - PostgreSQL gratuito (limitado)
  - Sleep después de inactividad (pero funciona)
- **Desventajas:** 
  - Se duerme si no recibe requests en 15 min
  - Limitado a 250MB de BD

**Setup:** https://render.com/docs/deploy-django

---

## 2. **PythonAnywhere** ⭐ (MEJOR PARA DJANGO)
- **Costo:** Gratuito (plan Beginner)
- **Ventajas:**
  - Específico para Python/Django
  - Incluye base de datos MySQL gratuita
  - **No se duerme** (siempre disponible)
  - SSL gratuito
  - Web console para ejecutar comandos
- **Desventajas:**
  - Interfaz menos moderna
  - Limitado a 100 requests/día en plan gratuito
  - No incluye PostgreSQL (solo MySQL)

**Setup:** https://www.pythonanywhere.com/
1. Sign up con GitHub
2. Upload código vía Git
3. Configura Django app
4. Listo

---

## 3. **Google Cloud Run** 💰 (BARATÍSIMO)
- **Costo:** $0.15 per million requests (muy barato)
- **Ventajas:**
  - Créditos gratuitos iniciales
  - Escalable automáticamente
  - No se duerme
  - Excelente performance
- **Desventajas:**
  - Más complejidad inicial
  - Requiere Cloud SQL (PostgreSQL)

**Setup:** Requiere Docker, más complejo

---

## 4. **Fly.io**
- **Costo:** $5/mes gratuitos + pago por uso
- **Ventajas:**
  - Deploy muy rápido
  - Buena performance
  - No se duerme
- **Desventajas:**
  - Después del crédito inicial, cuesta dinero

---

## 5. **Replit**
- **Costo:** Gratuito
- **Ventajas:**
  - Muy fácil de usar
  - IDE integrado
- **Desventajas:**
  - Muy lento
  - Se duerme frecuentemente
  - No recomendado para producción

---

## Mi recomendación: **PythonAnywhere** (Plan Beginner)

Para este proyecto, **PythonAnywhere** es la mejor opción porque:

1. ✅ **Totalmente gratis** en plan Beginner
2. ✅ **Específico para Django** (menos configuración)
3. ✅ **No se duerme** (siempre online)
4. ✅ **Incluye BD gratis** (MySQL)
5. ✅ **SSL automático** (https://tudominio.pythonanywhere.com)

### Limitaciones del plan gratuito:
- 100 requests/día
- 512 MB de almacenamiento
- MySQL solamente
- Sin dominio personalizado (pero es subdomain gratuito)

**Ideal para:** Dev/testing, MVP, proyecto pequeño

---

## Plan: Usar PythonAnywhere ahora, migrar después

```
Hoy                          Después (si crece)
┌─────────────────────┐      ┌──────────────────┐
│  PythonAnywhere     │ ──→  │  Google Cloud    │
│  (Gratuito)         │      │  Run o Railway   │
│  100 req/día        │      │  (Pago)          │
└─────────────────────┘      └──────────────────┘
```

---

## Quick Setup: PythonAnywhere

### Paso 1: Crear cuenta
1. Ve a https://www.pythonanywhere.com/
2. Click "Start running Python online in less than a minute!"
3. Sign up con GitHub o email

### Paso 2: Crear Web App
En el panel:
1. Click "Web" → "Add a new web app"
2. Selecciona "Python 3.11" + "Django"
3. PythonAnywhere crea un Django app básico

### Paso 3: Reemplazar con nuestro código
1. Click "Consoles" → "Bash console"
2. Ir a la carpeta del proyecto:
   ```bash
   cd /home/tu_usuario/mysite
   git clone https://github.com/tu_username/wlg-backend.git
   ```
3. Copiar archivos de nuestro backend

### Paso 4: Configurar base de datos
1. En PythonAnywhere, MySQL está automático
2. Ejecutar migraciones:
   ```bash
   python manage.py migrate
   ```

### Paso 5: Crear superusuario
```bash
python manage.py createsuperuser
```

### Paso 6: Reload
Click "Web" → "Reload" en tu web app

Tu API estará en: `https://tu_usuario.pythonanywhere.com/api/familias/`

---

## O usar **Render** (también gratuito)

Si prefieres Render:
1. https://render.com/
2. New → Web Service
3. Connect GitHub
4. Deploy automático
5. PostgreSQL gratuito (limitado)

Mismo setup pero un poco diferente.

---

## Decisión rápida

| Opción | Gratuito | Siempre online | Fácil | Ideal para |
|--------|----------|---|---|---|
| **PythonAnywhere** | ✅ Sí | ✅ Sí | ✅✅ Muy | Este proyecto |
| **Render** | ✅ Sí | ❌ Se duerme | ✅ Fácil | MVP rápido |
| **Google Cloud** | ✅ Créditos | ✅ Sí | ⚠️ Complejo | Escala |

---

## Recomendación final

**Usa PythonAnywhere para empezar**, es:
- Totalmente gratis
- Siempre online
- Hecho para Django
- Fácil de setupear

Después si crece el tráfico, migras a Google Cloud Run o Railway.

¿Arrancamos con PythonAnywhere?
