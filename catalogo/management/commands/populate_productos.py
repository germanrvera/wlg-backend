from django.core.management.base import BaseCommand
from catalogo.models import FamiliaProducto


# SKUs por familia — formato: {"cod": "CODIGO-SKU", "desc": "Descripción comercial"}
# cod sigue el patrón: FAMILIA-WATT-CCT-ACABADO  |  FAMILIA-LENGTHmm-CCT-ACABADO
# Acabados: N=Negro anodizado  B=Blanco  P=Plata anodizado  C=Cobre

PRODUCTOS = {

    # ── SISTEMAS DE RIEL ────────────────────────────────────────────────────
    "Galuy": [
        {"cod": "GALUY-10W-15-3000-N",  "desc": "Galuy 10W 15° 3000K Negro anodizado"},
        {"cod": "GALUY-10W-24-3000-N",  "desc": "Galuy 10W 24° 3000K Negro anodizado"},
        {"cod": "GALUY-10W-24-3000-B",  "desc": "Galuy 10W 24° 3000K Blanco"},
        {"cod": "GALUY-10W-24-2700-N",  "desc": "Galuy 10W 24° 2700K Negro anodizado"},
        {"cod": "GALUY-10W-36-3000-N",  "desc": "Galuy 10W 36° 3000K Negro anodizado"},
        {"cod": "GALUY-10W-36-3000-B",  "desc": "Galuy 10W 36° 3000K Blanco"},
        {"cod": "GALUY-20W-15-3000-N",  "desc": "Galuy 20W 15° 3000K Negro anodizado"},
        {"cod": "GALUY-20W-24-3000-N",  "desc": "Galuy 20W 24° 3000K Negro anodizado"},
        {"cod": "GALUY-20W-24-3000-B",  "desc": "Galuy 20W 24° 3000K Blanco"},
        {"cod": "GALUY-20W-24-4000-N",  "desc": "Galuy 20W 24° 4000K Negro anodizado"},
        {"cod": "GALUY-20W-36-3000-N",  "desc": "Galuy 20W 36° 3000K Negro anodizado"},
        {"cod": "GALUY-20W-36-4000-N",  "desc": "Galuy 20W 36° 4000K Negro anodizado"},
    ],

    "Cetus": [
        {"cod": "CETUS-12W-24-3000-N",  "desc": "Cetus 12W 24° 3000K Negro anodizado"},
        {"cod": "CETUS-12W-24-3000-B",  "desc": "Cetus 12W 24° 3000K Blanco"},
        {"cod": "CETUS-12W-24-2700-N",  "desc": "Cetus 12W 24° 2700K Negro anodizado"},
        {"cod": "CETUS-12W-36-3000-N",  "desc": "Cetus 12W 36° 3000K Negro anodizado"},
        {"cod": "CETUS-25W-24-3000-N",  "desc": "Cetus 25W 24° 3000K Negro anodizado"},
        {"cod": "CETUS-25W-24-3000-B",  "desc": "Cetus 25W 24° 3000K Blanco"},
        {"cod": "CETUS-25W-24-4000-N",  "desc": "Cetus 25W 24° 4000K Negro anodizado"},
        {"cod": "CETUS-25W-36-3000-N",  "desc": "Cetus 25W 36° 3000K Negro anodizado"},
        {"cod": "CETUS-25W-60-3000-N",  "desc": "Cetus 25W 60° 3000K Negro anodizado"},
    ],

    "Lira": [
        {"cod": "LIRA-15W-24-3000-N",   "desc": "Lira 15W 24° 3000K Negro anodizado"},
        {"cod": "LIRA-15W-24-3000-B",   "desc": "Lira 15W 24° 3000K Blanco"},
        {"cod": "LIRA-15W-24-2700-N",   "desc": "Lira 15W 24° 2700K Negro anodizado"},
        {"cod": "LIRA-15W-36-3000-N",   "desc": "Lira 15W 36° 3000K Negro anodizado"},
        {"cod": "LIRA-30W-24-3000-N",   "desc": "Lira 30W 24° 3000K Negro anodizado"},
        {"cod": "LIRA-30W-24-3000-B",   "desc": "Lira 30W 24° 3000K Blanco"},
        {"cod": "LIRA-30W-24-4000-N",   "desc": "Lira 30W 24° 4000K Negro anodizado"},
        {"cod": "LIRA-30W-36-3000-N",   "desc": "Lira 30W 36° 3000K Negro anodizado"},
    ],

    "Orion": [
        {"cod": "ORION-20W-15-3000-N",  "desc": "Orion 20W 15° 3000K Negro anodizado"},
        {"cod": "ORION-20W-24-3000-N",  "desc": "Orion 20W 24° 3000K Negro anodizado"},
        {"cod": "ORION-20W-24-3000-B",  "desc": "Orion 20W 24° 3000K Blanco"},
        {"cod": "ORION-20W-24-2700-N",  "desc": "Orion 20W 24° 2700K Negro anodizado"},
        {"cod": "ORION-35W-15-3000-N",  "desc": "Orion 35W 15° 3000K Negro anodizado"},
        {"cod": "ORION-35W-24-3000-N",  "desc": "Orion 35W 24° 3000K Negro anodizado"},
        {"cod": "ORION-35W-24-3000-B",  "desc": "Orion 35W 24° 3000K Blanco"},
        {"cod": "ORION-35W-24-4000-N",  "desc": "Orion 35W 24° 4000K Negro anodizado"},
        {"cod": "ORION-50W-15-3000-N",  "desc": "Orion 50W 15° 3000K Negro anodizado"},
        {"cod": "ORION-50W-24-3000-N",  "desc": "Orion 50W 24° 3000K Negro anodizado"},
    ],

    # ── ILUMINACIÓN LINEAL ──────────────────────────────────────────────────
    "Petra": [
        {"cod": "PETRA-300MM-3000-N",   "desc": "Petra Lineal Empotrada 300mm 3000K Negro"},
        {"cod": "PETRA-300MM-3000-B",   "desc": "Petra Lineal Empotrada 300mm 3000K Blanco"},
        {"cod": "PETRA-300MM-2700-N",   "desc": "Petra Lineal Empotrada 300mm 2700K Negro"},
        {"cod": "PETRA-600MM-3000-N",   "desc": "Petra Lineal Empotrada 600mm 3000K Negro"},
        {"cod": "PETRA-600MM-3000-B",   "desc": "Petra Lineal Empotrada 600mm 3000K Blanco"},
        {"cod": "PETRA-600MM-2700-N",   "desc": "Petra Lineal Empotrada 600mm 2700K Negro"},
        {"cod": "PETRA-600MM-4000-N",   "desc": "Petra Lineal Empotrada 600mm 4000K Negro"},
        {"cod": "PETRA-1200MM-3000-N",  "desc": "Petra Lineal Empotrada 1200mm 3000K Negro"},
        {"cod": "PETRA-1200MM-3000-B",  "desc": "Petra Lineal Empotrada 1200mm 3000K Blanco"},
        {"cod": "PETRA-1200MM-2700-N",  "desc": "Petra Lineal Empotrada 1200mm 2700K Negro"},
        {"cod": "PETRA-1200MM-4000-N",  "desc": "Petra Lineal Empotrada 1200mm 4000K Negro"},
    ],

    "Sirio": [
        {"cod": "SIRIO-300MM-3000-N",   "desc": "Sirio Lineal Superficie 300mm 3000K Negro"},
        {"cod": "SIRIO-300MM-3000-B",   "desc": "Sirio Lineal Superficie 300mm 3000K Blanco"},
        {"cod": "SIRIO-600MM-3000-N",   "desc": "Sirio Lineal Superficie 600mm 3000K Negro"},
        {"cod": "SIRIO-600MM-3000-B",   "desc": "Sirio Lineal Superficie 600mm 3000K Blanco"},
        {"cod": "SIRIO-600MM-2700-N",   "desc": "Sirio Lineal Superficie 600mm 2700K Negro"},
        {"cod": "SIRIO-1200MM-3000-N",  "desc": "Sirio Lineal Superficie 1200mm 3000K Negro"},
        {"cod": "SIRIO-1200MM-3000-B",  "desc": "Sirio Lineal Superficie 1200mm 3000K Blanco"},
        {"cod": "SIRIO-1200MM-2700-N",  "desc": "Sirio Lineal Superficie 1200mm 2700K Negro"},
        {"cod": "SIRIO-1200MM-4000-N",  "desc": "Sirio Lineal Superficie 1200mm 4000K Negro"},
    ],

    "Vega": [
        {"cod": "VEGA-600MM-3000-N",    "desc": "Vega Lineal Suspendida 600mm 3000K Negro"},
        {"cod": "VEGA-600MM-3000-B",    "desc": "Vega Lineal Suspendida 600mm 3000K Blanco"},
        {"cod": "VEGA-600MM-2700-N",    "desc": "Vega Lineal Suspendida 600mm 2700K Negro"},
        {"cod": "VEGA-1200MM-3000-N",   "desc": "Vega Lineal Suspendida 1200mm 3000K Negro"},
        {"cod": "VEGA-1200MM-3000-B",   "desc": "Vega Lineal Suspendida 1200mm 3000K Blanco"},
        {"cod": "VEGA-1200MM-2700-N",   "desc": "Vega Lineal Suspendida 1200mm 2700K Negro"},
        {"cod": "VEGA-1200MM-4000-N",   "desc": "Vega Lineal Suspendida 1200mm 4000K Negro"},
        {"cod": "VEGA-1800MM-3000-N",   "desc": "Vega Lineal Suspendida 1800mm 3000K Negro"},
        {"cod": "VEGA-1800MM-3000-B",   "desc": "Vega Lineal Suspendida 1800mm 3000K Blanco"},
    ],

    # ── SISTEMAS ESPECIALES ─────────────────────────────────────────────────
    "Nova": [
        {"cod": "NOVA-30W-24-3000-N",   "desc": "Nova Sistema Modular 30W 24° 3000K Negro anodizado"},
        {"cod": "NOVA-30W-24-3000-B",   "desc": "Nova Sistema Modular 30W 24° 3000K Blanco"},
        {"cod": "NOVA-30W-36-3000-N",   "desc": "Nova Sistema Modular 30W 36° 3000K Negro anodizado"},
        {"cod": "NOVA-30W-24-2700-N",   "desc": "Nova Sistema Modular 30W 24° 2700K Negro anodizado"},
        {"cod": "NOVA-60W-24-3000-N",   "desc": "Nova Sistema Modular 60W 24° 3000K Negro anodizado"},
        {"cod": "NOVA-60W-24-3000-B",   "desc": "Nova Sistema Modular 60W 24° 3000K Blanco"},
        {"cod": "NOVA-60W-24-4000-N",   "desc": "Nova Sistema Modular 60W 24° 4000K Negro anodizado"},
        {"cod": "NOVA-60W-36-3000-N",   "desc": "Nova Sistema Modular 60W 36° 3000K Negro anodizado"},
    ],

    "Altair": [
        {"cod": "ALTAIR-25W-15-3000-N", "desc": "Altair 25W 15° 3000K Negro anodizado"},
        {"cod": "ALTAIR-25W-24-3000-N", "desc": "Altair 25W 24° 3000K Negro anodizado"},
        {"cod": "ALTAIR-25W-24-3000-B", "desc": "Altair 25W 24° 3000K Blanco"},
        {"cod": "ALTAIR-25W-24-2700-N", "desc": "Altair 25W 24° 2700K Negro anodizado"},
        {"cod": "ALTAIR-50W-15-3000-N", "desc": "Altair 50W 15° 3000K Negro anodizado"},
        {"cod": "ALTAIR-50W-24-3000-N", "desc": "Altair 50W 24° 3000K Negro anodizado"},
        {"cod": "ALTAIR-50W-24-4000-N", "desc": "Altair 50W 24° 4000K Negro anodizado"},
        {"cod": "ALTAIR-50W-36-3000-N", "desc": "Altair 50W 36° 3000K Negro anodizado"},
    ],

    # ── ARTEFACTOS Y APLIQUES ───────────────────────────────────────────────
    "Lyra": [
        {"cod": "LYRA-15W-3000-N",      "desc": "Lyra Aplique 15W 3000K Negro"},
        {"cod": "LYRA-15W-3000-B",      "desc": "Lyra Aplique 15W 3000K Blanco"},
        {"cod": "LYRA-15W-2700-N",      "desc": "Lyra Aplique 15W 2700K Negro"},
        {"cod": "LYRA-15W-2700-B",      "desc": "Lyra Aplique 15W 2700K Blanco"},
        {"cod": "LYRA-25W-3000-N",      "desc": "Lyra Aplique 25W 3000K Negro"},
        {"cod": "LYRA-25W-3000-B",      "desc": "Lyra Aplique 25W 3000K Blanco"},
        {"cod": "LYRA-25W-2700-N",      "desc": "Lyra Aplique 25W 2700K Negro"},
    ],

    "Deneb": [
        {"cod": "DENEB-20W-3000-N",     "desc": "Deneb Downlight 20W 3000K Negro"},
        {"cod": "DENEB-20W-3000-B",     "desc": "Deneb Downlight 20W 3000K Blanco"},
        {"cod": "DENEB-20W-2700-N",     "desc": "Deneb Downlight 20W 2700K Negro"},
        {"cod": "DENEB-20W-2700-B",     "desc": "Deneb Downlight 20W 2700K Blanco"},
        {"cod": "DENEB-40W-3000-N",     "desc": "Deneb Downlight 40W 3000K Negro"},
        {"cod": "DENEB-40W-3000-B",     "desc": "Deneb Downlight 40W 3000K Blanco"},
        {"cod": "DENEB-40W-2700-N",     "desc": "Deneb Downlight 40W 2700K Negro"},
        {"cod": "DENEB-40W-4000-N",     "desc": "Deneb Downlight 40W 4000K Negro"},
    ],

    "Castor": [
        {"cod": "CASTOR-10W-3000-N",    "desc": "Castor Aplique Mural 10W 3000K Negro"},
        {"cod": "CASTOR-10W-3000-B",    "desc": "Castor Aplique Mural 10W 3000K Blanco"},
        {"cod": "CASTOR-10W-2700-N",    "desc": "Castor Aplique Mural 10W 2700K Negro"},
        {"cod": "CASTOR-20W-3000-N",    "desc": "Castor Aplique Mural 20W 3000K Negro"},
        {"cod": "CASTOR-20W-3000-B",    "desc": "Castor Aplique Mural 20W 3000K Blanco"},
        {"cod": "CASTOR-20W-2700-N",    "desc": "Castor Aplique Mural 20W 2700K Negro"},
    ],

    # ── EXTERIOR ────────────────────────────────────────────────────────────
    "Rigel": [
        {"cod": "RIGEL-15W-3000-N-IP65",  "desc": "Rigel Proyector Exterior 15W 3000K Negro IP65"},
        {"cod": "RIGEL-15W-4000-N-IP65",  "desc": "Rigel Proyector Exterior 15W 4000K Negro IP65"},
        {"cod": "RIGEL-30W-3000-N-IP65",  "desc": "Rigel Proyector Exterior 30W 3000K Negro IP65"},
        {"cod": "RIGEL-30W-4000-N-IP65",  "desc": "Rigel Proyector Exterior 30W 4000K Negro IP65"},
        {"cod": "RIGEL-50W-3000-N-IP65",  "desc": "Rigel Proyector Exterior 50W 3000K Negro IP65"},
        {"cod": "RIGEL-50W-4000-N-IP65",  "desc": "Rigel Proyector Exterior 50W 4000K Negro IP65"},
        {"cod": "RIGEL-100W-3000-N-IP65", "desc": "Rigel Proyector Exterior 100W 3000K Negro IP65"},
        {"cod": "RIGEL-100W-4000-N-IP65", "desc": "Rigel Proyector Exterior 100W 4000K Negro IP65"},
    ],

    "Mira": [
        {"cod": "MIRA-10W-3000-N-IP65",  "desc": "Mira Aplique Exterior 10W 3000K Negro IP65"},
        {"cod": "MIRA-10W-3000-B-IP65",  "desc": "Mira Aplique Exterior 10W 3000K Blanco IP65"},
        {"cod": "MIRA-10W-4000-N-IP65",  "desc": "Mira Aplique Exterior 10W 4000K Negro IP65"},
        {"cod": "MIRA-20W-3000-N-IP65",  "desc": "Mira Aplique Exterior 20W 3000K Negro IP65"},
        {"cod": "MIRA-20W-3000-B-IP65",  "desc": "Mira Aplique Exterior 20W 3000K Blanco IP65"},
        {"cod": "MIRA-20W-4000-N-IP65",  "desc": "Mira Aplique Exterior 20W 4000K Negro IP65"},
        {"cod": "MIRA-35W-3000-N-IP65",  "desc": "Mira Aplique Exterior 35W 3000K Negro IP65"},
        {"cod": "MIRA-35W-4000-N-IP65",  "desc": "Mira Aplique Exterior 35W 4000K Negro IP65"},
    ],

    # ── MÓDULOS ─────────────────────────────────────────────────────────────
    "Canopus": [
        {"cod": "CANOPUS-MOD-2700",     "desc": "Canopus Módulo LED 2700K"},
        {"cod": "CANOPUS-MOD-3000",     "desc": "Canopus Módulo LED 3000K"},
        {"cod": "CANOPUS-MOD-4000",     "desc": "Canopus Módulo LED 4000K"},
        {"cod": "CANOPUS-MOD-CCT",      "desc": "Canopus Módulo LED CCT Tunable (2700K–4000K)"},
        {"cod": "CANOPUS-MOD-2700-HO",  "desc": "Canopus Módulo LED 2700K High Output"},
        {"cod": "CANOPUS-MOD-3000-HO",  "desc": "Canopus Módulo LED 3000K High Output"},
        {"cod": "CANOPUS-MOD-4000-HO",  "desc": "Canopus Módulo LED 4000K High Output"},
    ],

    "Pollux": [
        {"cod": "POLLUX-MOD-2700",      "desc": "Pollux Módulo LED 2700K"},
        {"cod": "POLLUX-MOD-3000",      "desc": "Pollux Módulo LED 3000K"},
        {"cod": "POLLUX-MOD-4000",      "desc": "Pollux Módulo LED 4000K"},
        {"cod": "POLLUX-MOD-CCT",       "desc": "Pollux Módulo LED CCT Tunable (2700K–4000K)"},
        {"cod": "POLLUX-MOD-2700-HO",   "desc": "Pollux Módulo LED 2700K High Output"},
        {"cod": "POLLUX-MOD-3000-HO",   "desc": "Pollux Módulo LED 3000K High Output"},
    ],
}


class Command(BaseCommand):
    help = 'Populate productos field for all FamiliaProducto records'

    def handle(self, *args, **options):
        updated = 0
        skipped = 0
        for nombre, productos in PRODUCTOS.items():
            try:
                fam = FamiliaProducto.objects.get(nombre=nombre)
                fam.productos = productos
                fam.skus = len(productos)
                fam.save(update_fields=['productos', 'skus'])
                self.stdout.write(self.style.SUCCESS(
                    f'  {nombre}: {len(productos)} SKUs cargados'
                ))
                updated += 1
            except FamiliaProducto.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f'  {nombre}: familia no encontrada en DB — omitida'
                ))
                skipped += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nListo: {updated} familias actualizadas, {skipped} omitidas.'
        ))
