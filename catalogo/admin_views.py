import openpyxl
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import FamiliaProducto, Producto

# Maps 'Sección' column in the Excel → FamiliaProducto.nombre in the database.
# Rows with an unmapped sección are skipped (counted as "omitidos").
SECCION_FAMILIA_MAP = {
    'Artefactos':                 'Artefactos',
    'Artefactos LED incorporado': 'Artefactos LED Incorporado',
    'Artefactos de exterior':     'Exterior',
    'Fuentes':                    'Fuentes',
    'Intervención de fachadas':   'Intervención de fachadas',
    'Linea Hogar':                'Línea Hogar',
    'Micro Runner':               'Micro Runner',
    'Micro Track':                'Micro Track M7',
    'Módulos LED':                'Módulos LED',
    'Perfiles Linear':            'Linear',
    'Perfiles Linear Slim':       'Linear Slim',
    'Perfiles Portaled':          'Perfiles Portaled',
    'Powergear':                  'Fuentes',
    'Runner':                     'Runner',
    'Sistema de control':         'Sistemas de control',
    'Tiras Jenny':                'Jenny',
    'Tiras LED':                  'Tiras LED',
    'Track LV':                   'Track LV',
    'Tracklights 220V':           'Track Lights 220V',
    'Wally':                      'Wally',
    # 'Productos discontinuos' is intentionally omitted → skipped
}

# Column indices in the 'Productos' sheet (1-based)
COL_CODIGO   = 1   # Código Lista
COL_SECCION  = 3   # Sección
COL_DESC     = 5   # Descripción
COL_CT       = 6   # CT
COL_CRI      = 7   # CRI
COL_WPM      = 8   # W/M  (tiras por metro)
COL_LMPM     = 9   # Lm/M (tiras por metro)
COL_V        = 11  # V
COL_IP       = 12  # IP
COL_DIM      = 13  # Dim.
COL_DIM_SYS  = 14  # Sist. Dim.
COL_ANG      = 15  # Ang.
COL_W        = 16  # W   (artefactos, valor total)
COL_LM       = 17  # Lm  (artefactos, valor total)
COL_ACABADO  = 28  # Acabado


def _s(val):
    if val is None:
        return ''
    return str(val).strip()


def _dim(val):
    s = _s(val).lower()
    if s.startswith('s'):   # Sí / Si / Sí* / Si*
        return 'Sí'
    if s in ('no', '-'):
        return 'No'
    return ''


@staff_member_required
def import_excel_view(request):
    ctx = {
        'title': 'Importar Productos desde Excel',
        'opts': Producto._meta,
        'has_permission': True,
    }

    if request.method != 'POST':
        return render(request, 'admin/catalogo/import_excel.html', ctx)

    upload = request.FILES.get('excel_file')
    if not upload:
        messages.error(request, 'No se seleccionó ningún archivo.')
        return render(request, 'admin/catalogo/import_excel.html', ctx)

    try:
        wb = openpyxl.load_workbook(upload, data_only=True)
    except Exception as exc:
        messages.error(request, f'No se pudo abrir el archivo: {exc}')
        return render(request, 'admin/catalogo/import_excel.html', ctx)

    if 'Productos' not in wb.sheetnames:
        messages.error(request, "El archivo no tiene una hoja llamada 'Productos'.")
        return render(request, 'admin/catalogo/import_excel.html', ctx)

    ws = wb['Productos']

    # Cache all families once to avoid N+1 queries
    familias = {f.nombre: f for f in FamiliaProducto.objects.all()}

    created = updated = skipped = 0
    row_errors = []

    for row_num in range(2, ws.max_row + 1):
        codigo = _s(ws.cell(row_num, COL_CODIGO).value)
        if not codigo:
            continue

        seccion = _s(ws.cell(row_num, COL_SECCION).value)
        familia_nombre = SECCION_FAMILIA_MAP.get(seccion)
        if not familia_nombre:
            skipped += 1
            continue

        familia = familias.get(familia_nombre)
        if not familia:
            row_errors.append(
                f'Fila {row_num} ({codigo}): familia "{familia_nombre}" no existe en la BD.'
            )
            skipped += 1
            continue

        # W and Lm: use W/M for tiras (per-meter), W for artefactos (total)
        wpm  = _s(ws.cell(row_num, COL_WPM).value)
        lmpm = _s(ws.cell(row_num, COL_LMPM).value)

        defaults = {
            'familia':    familia,
            'descripcion': _s(ws.cell(row_num, COL_DESC).value),
            'ct':         _s(ws.cell(row_num, COL_CT).value),
            'cri':        _s(ws.cell(row_num, COL_CRI).value),
            'w':          wpm or _s(ws.cell(row_num, COL_W).value),
            'lm':         lmpm or _s(ws.cell(row_num, COL_LM).value),
            'v':          _s(ws.cell(row_num, COL_V).value),
            'ip':         _s(ws.cell(row_num, COL_IP).value),
            'dim':        _dim(ws.cell(row_num, COL_DIM).value),
            'dim_sys':    _s(ws.cell(row_num, COL_DIM_SYS).value),
            'angulo':     _s(ws.cell(row_num, COL_ANG).value),
            'acabado':    _s(ws.cell(row_num, COL_ACABADO).value),
        }

        _, was_created = Producto.objects.update_or_create(codigo=codigo, defaults=defaults)
        if was_created:
            created += 1
        else:
            updated += 1

    level = messages.SUCCESS if not row_errors else messages.WARNING
    messages.add_message(
        request, level,
        f'Importación completada — '
        f'✔ Creados: {created} | ↺ Actualizados: {updated} | ⊘ Omitidos: {skipped}',
    )
    for err in row_errors[:20]:
        messages.warning(request, err)
    if len(row_errors) > 20:
        messages.warning(request, f'... y {len(row_errors) - 20} errores más.')

    return redirect(reverse('admin:catalogo_producto_changelist'))
