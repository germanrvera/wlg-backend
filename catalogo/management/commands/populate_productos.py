from django.core.management.base import BaseCommand
from catalogo.models import FamiliaProducto, Producto


# SKUs por familia — coinciden con los nombres exactos en load_initial_data.py
# Patrón: FAMILIA-VARIANTE-CCT  |  FAMILIA-W-ANGULO-CCT-ACABADO
# Acabados: N=Negro  B=Blanco  P=Plata  G=Grafito

PRODUCTOS = {

    # ── TIRAS LED ARQ ────────────────────────────────────────────────────────
    "TIRAS LED ARQ": [
        {"cod": "TILARQ-4.8W-2700-24V",   "desc": "Tira LED Arq 4.8W/m 2700K 24V CRI≥90"},
        {"cod": "TILARQ-4.8W-3000-24V",   "desc": "Tira LED Arq 4.8W/m 3000K 24V CRI≥90"},
        {"cod": "TILARQ-4.8W-4000-24V",   "desc": "Tira LED Arq 4.8W/m 4000K 24V CRI≥80"},
        {"cod": "TILARQ-9.6W-2700-24V",   "desc": "Tira LED Arq 9.6W/m 2700K 24V CRI≥90"},
        {"cod": "TILARQ-9.6W-3000-24V",   "desc": "Tira LED Arq 9.6W/m 3000K 24V CRI≥90"},
        {"cod": "TILARQ-9.6W-4000-24V",   "desc": "Tira LED Arq 9.6W/m 4000K 24V CRI≥80"},
        {"cod": "TILARQ-14.4W-2700-24V",  "desc": "Tira LED Arq 14.4W/m 2700K 24V CRI≥90"},
        {"cod": "TILARQ-14.4W-3000-24V",  "desc": "Tira LED Arq 14.4W/m 3000K 24V CRI≥90"},
        {"cod": "TILARQ-14.4W-4000-24V",  "desc": "Tira LED Arq 14.4W/m 4000K 24V CRI≥80"},
        {"cod": "TILARQ-19.2W-3000-24V",  "desc": "Tira LED Arq 19.2W/m 3000K 24V CRI≥90"},
        {"cod": "TILARQ-CCT-9.6W-24V",    "desc": "Tira LED Arq 9.6W/m CCT Dinámico 24V DALI"},
        {"cod": "TILARQ-CCT-14.4W-24V",   "desc": "Tira LED Arq 14.4W/m CCT Dinámico 24V DALI"},
        {"cod": "TILARQ-4.8W-3000-IP65",  "desc": "Tira LED Arq 4.8W/m 3000K IP65 exterior"},
        {"cod": "TILARQ-9.6W-3000-IP65",  "desc": "Tira LED Arq 9.6W/m 3000K IP65 exterior"},
        {"cod": "TILARQ-RGBW-14.4W-24V",  "desc": "Tira LED Arq RGBW 14.4W/m 24V DMX"},
        {"cod": "TILARQ-34W-3000-IP33",   "desc": "Tira LED Arq 34W/m 3000K IP33 alta densidad"},
    ],

    # ── TIRAS LED HOGAR ──────────────────────────────────────────────────────
    "TIRAS LED HOGAR": [
        {"cod": "TILHOG-4.4W-2700-12V",   "desc": "Tira LED Hogar 4.4W/m 2700K 12V"},
        {"cod": "TILHOG-4.4W-3000-12V",   "desc": "Tira LED Hogar 4.4W/m 3000K 12V"},
        {"cod": "TILHOG-7.2W-3000-12V",   "desc": "Tira LED Hogar 7.2W/m 3000K 12V"},
        {"cod": "TILHOG-7.2W-4000-12V",   "desc": "Tira LED Hogar 7.2W/m 4000K 12V"},
        {"cod": "TILHOG-9.6W-3000-12V",   "desc": "Tira LED Hogar 9.6W/m 3000K 12V"},
        {"cod": "TILHOG-CCT-9.6W-12V",    "desc": "Tira LED Hogar 9.6W/m CCT Dinámico 12V"},
        {"cod": "TILHOG-19.2W-3000-12V",  "desc": "Tira LED Hogar 19.2W/m 3000K 12V alta potencia"},
        {"cod": "TILHOG-RGB-12W-12V",     "desc": "Tira LED Hogar RGB 12W/m 12V control WiFi"},
    ],

    # ── PERFILES PORTALED ────────────────────────────────────────────────────
    "PERFILES PORTALED": [
        {"cod": "PERF-EMP-15-N",    "desc": "Perfil PortaLED empotrado 15mm anodizado negro"},
        {"cod": "PERF-EMP-15-B",    "desc": "Perfil PortaLED empotrado 15mm blanco"},
        {"cod": "PERF-EMP-20-N",    "desc": "Perfil PortaLED empotrado 20mm anodizado negro"},
        {"cod": "PERF-EMP-20-B",    "desc": "Perfil PortaLED empotrado 20mm blanco"},
        {"cod": "PERF-SUP-20-N",    "desc": "Perfil PortaLED superficie 20mm anodizado negro"},
        {"cod": "PERF-SUP-20-B",    "desc": "Perfil PortaLED superficie 20mm blanco"},
        {"cod": "PERF-ESQ-N",       "desc": "Perfil PortaLED esquinero 45° anodizado negro"},
        {"cod": "PERF-ESQ-B",       "desc": "Perfil PortaLED esquinero 45° blanco"},
        {"cod": "PERF-COL-N",       "desc": "Perfil PortaLED colgante suspendido negro"},
        {"cod": "PERF-COL-B",       "desc": "Perfil PortaLED colgante suspendido blanco"},
    ],

    # ── JENNY ────────────────────────────────────────────────────────────────
    "JENNY": [
        {"cod": "JENNY-5W-24-2700-N",   "desc": "Jenny 5W 24° 2700K Negro IP65"},
        {"cod": "JENNY-5W-24-3000-N",   "desc": "Jenny 5W 24° 3000K Negro IP65"},
        {"cod": "JENNY-5W-24-3000-B",   "desc": "Jenny 5W 24° 3000K Blanco IP65"},
        {"cod": "JENNY-5W-36-3000-N",   "desc": "Jenny 5W 36° 3000K Negro IP65"},
        {"cod": "JENNY-10W-15-3000-N",  "desc": "Jenny 10W 15° 3000K Negro IP65"},
        {"cod": "JENNY-10W-24-2700-N",  "desc": "Jenny 10W 24° 2700K Negro IP65"},
        {"cod": "JENNY-10W-24-3000-N",  "desc": "Jenny 10W 24° 3000K Negro IP65"},
        {"cod": "JENNY-10W-24-3000-B",  "desc": "Jenny 10W 24° 3000K Blanco IP65"},
        {"cod": "JENNY-10W-36-3000-N",  "desc": "Jenny 10W 36° 3000K Negro IP65"},
        {"cod": "JENNY-20W-15-3000-N",  "desc": "Jenny 20W 15° 3000K Negro IP65"},
        {"cod": "JENNY-20W-24-3000-N",  "desc": "Jenny 20W 24° 3000K Negro IP65"},
        {"cod": "JENNY-20W-24-3000-B",  "desc": "Jenny 20W 24° 3000K Blanco IP65"},
        {"cod": "JENNY-20W-24-4000-N",  "desc": "Jenny 20W 24° 4000K Negro IP65"},
        {"cod": "JENNY-20W-36-3000-N",  "desc": "Jenny 20W 36° 3000K Negro IP65"},
        {"cod": "JENNY-CCT-10W-24-N",   "desc": "Jenny CCT 10W 24° Dinámico DALI Negro IP65"},
        {"cod": "JENNY-CCT-20W-24-N",   "desc": "Jenny CCT 20W 24° Dinámico DALI Negro IP65"},
        {"cod": "JENNY-5W-24-2700-48V", "desc": "Jenny 5W 24° 2700K Negro 48V IP65"},
        {"cod": "JENNY-10W-24-3000-48V","desc": "Jenny 10W 24° 3000K Negro 48V IP65"},
    ],

    # ── FUENTES ──────────────────────────────────────────────────────────────
    "FUENTES": [
        {"cod": "FUENTE-12V-30W",       "desc": "Fuente switching 12V 30W IP20"},
        {"cod": "FUENTE-12V-60W",       "desc": "Fuente switching 12V 60W IP20"},
        {"cod": "FUENTE-12V-100W",      "desc": "Fuente switching 12V 100W IP20"},
        {"cod": "FUENTE-12V-150W",      "desc": "Fuente switching 12V 150W IP20"},
        {"cod": "FUENTE-24V-30W",       "desc": "Fuente switching 24V 30W IP20"},
        {"cod": "FUENTE-24V-60W",       "desc": "Fuente switching 24V 60W IP20"},
        {"cod": "FUENTE-24V-100W",      "desc": "Fuente switching 24V 100W IP20"},
        {"cod": "FUENTE-24V-150W",      "desc": "Fuente switching 24V 150W IP20"},
        {"cod": "FUENTE-24V-200W",      "desc": "Fuente switching 24V 200W IP20"},
        {"cod": "FUENTE-48V-60W",       "desc": "Fuente switching 48V 60W IP20"},
        {"cod": "FUENTE-48V-100W",      "desc": "Fuente switching 48V 100W IP20"},
        {"cod": "FUENTE-DIM-24V-60W",   "desc": "Fuente regulable TRIAC 24V 60W IP20"},
        {"cod": "FUENTE-DIM-24V-100W",  "desc": "Fuente regulable 1-10V 24V 100W IP20"},
        {"cod": "FUENTE-DALI-24V-60W",  "desc": "Fuente DALI 24V 60W IP20"},
        {"cod": "FUENTE-DALI-24V-100W", "desc": "Fuente DALI 24V 100W IP20"},
        {"cod": "FUENTE-DALI-24V-200W", "desc": "Fuente DALI 24V 200W IP20"},
        {"cod": "FUENTE-12V-60W-DIM",   "desc": "Fuente regulable TRIAC 12V 60W IP20"},
        {"cod": "FUENTE-24V-150W-DIM",  "desc": "Fuente regulable 1-10V 24V 150W IP20"},
    ],

    # ── LÁMPARAS ─────────────────────────────────────────────────────────────
    "LÁMPARAS": [
        {"cod": "LAM-GU10-5W-2700",     "desc": "Lámpara GU10 5W 2700K CRI≥90 regulable"},
        {"cod": "LAM-GU10-5W-3000",     "desc": "Lámpara GU10 5W 3000K CRI≥90 regulable"},
        {"cod": "LAM-GU10-7W-2700",     "desc": "Lámpara GU10 7W 2700K CRI≥90 regulable"},
        {"cod": "LAM-GU10-7W-3000",     "desc": "Lámpara GU10 7W 3000K CRI≥90 regulable"},
        {"cod": "LAM-GU10-10W-3000",    "desc": "Lámpara GU10 10W 3000K CRI≥80 regulable"},
        {"cod": "LAM-E27-5W-2700",      "desc": "Lámpara E27 5W 2700K CRI≥90 regulable"},
        {"cod": "LAM-E27-8W-2700",      "desc": "Lámpara E27 8W 2700K CRI≥90 regulable"},
        {"cod": "LAM-E27-8W-3000",      "desc": "Lámpara E27 8W 3000K CRI≥90 regulable"},
        {"cod": "LAM-E27-12W-3000",     "desc": "Lámpara E27 12W 3000K CRI≥80 regulable"},
        {"cod": "LAM-E27-15W-3000",     "desc": "Lámpara E27 15W 3000K CRI≥80 regulable"},
        {"cod": "LAM-AR111-10W-3000",   "desc": "Lámpara AR111 10W 3000K 25° CRI≥80"},
        {"cod": "LAM-AR111-15W-3000",   "desc": "Lámpara AR111 15W 3000K 25° CRI≥90"},
        {"cod": "LAM-AR111-15W-2700",   "desc": "Lámpara AR111 15W 2700K 25° CRI≥90"},
    ],

    # ── ARTEFACTOS GU/AR ─────────────────────────────────────────────────────
    "ARTEFACTOS GU/AR": [
        {"cod": "ARG-1GU10-SUP-N",      "desc": "Artefacto 1xGU10 superficie negro"},
        {"cod": "ARG-1GU10-SUP-B",      "desc": "Artefacto 1xGU10 superficie blanco"},
        {"cod": "ARG-2GU10-SUP-N",      "desc": "Artefacto 2xGU10 superficie negro"},
        {"cod": "ARG-1AR111-SUP-N",     "desc": "Artefacto 1xAR111 superficie negro"},
        {"cod": "ARG-1AR111-INC-N",     "desc": "Artefacto 1xAR111 inclinado 30° negro"},
        {"cod": "ARG-1AR111-INC-B",     "desc": "Artefacto 1xAR111 inclinado 30° blanco"},
    ],

    # ── KATAN ────────────────────────────────────────────────────────────────
    "KATAN": [
        {"cod": "KATAN-3W-2700-N",      "desc": "Katan 3W 2700K Negro IP44 CRI≥80"},
        {"cod": "KATAN-3W-3000-N",      "desc": "Katan 3W 3000K Negro IP44 CRI≥80"},
        {"cod": "KATAN-5W-2700-N",      "desc": "Katan 5W 2700K Negro IP44 CRI≥90"},
        {"cod": "KATAN-5W-3000-N",      "desc": "Katan 5W 3000K Negro IP44 CRI≥90"},
        {"cod": "KATAN-5W-3000-B",      "desc": "Katan 5W 3000K Blanco IP44 CRI≥90"},
        {"cod": "KATAN-5W-2700-B",      "desc": "Katan 5W 2700K Blanco IP44 CRI≥95"},
    ],

    # ── MICRO RUNNER ─────────────────────────────────────────────────────────
    "MICRO RUNNER": [
        {"cod": "MR-2W-24-2700-N",      "desc": "Micro Runner 2W 24° 2700K Negro CRI≥90"},
        {"cod": "MR-2W-24-3000-N",      "desc": "Micro Runner 2W 24° 3000K Negro CRI≥90"},
        {"cod": "MR-5W-15-3000-N",      "desc": "Micro Runner 5W 15° 3000K Negro CRI≥90"},
        {"cod": "MR-5W-24-2700-N",      "desc": "Micro Runner 5W 24° 2700K Negro CRI≥90"},
        {"cod": "MR-5W-24-3000-N",      "desc": "Micro Runner 5W 24° 3000K Negro CRI≥90"},
        {"cod": "MR-5W-24-3000-B",      "desc": "Micro Runner 5W 24° 3000K Blanco CRI≥90"},
        {"cod": "MR-5W-36-3000-N",      "desc": "Micro Runner 5W 36° 3000K Negro CRI≥80"},
        {"cod": "MR-10W-15-3000-N",     "desc": "Micro Runner 10W 15° 3000K Negro DALI"},
        {"cod": "MR-10W-24-2700-N",     "desc": "Micro Runner 10W 24° 2700K Negro DALI"},
        {"cod": "MR-10W-24-3000-N",     "desc": "Micro Runner 10W 24° 3000K Negro DALI"},
        {"cod": "MR-10W-24-3000-B",     "desc": "Micro Runner 10W 24° 3000K Blanco DALI"},
        {"cod": "MR-10W-36-3000-N",     "desc": "Micro Runner 10W 36° 3000K Negro"},
        {"cod": "MR-20W-15-3000-N",     "desc": "Micro Runner 20W 15° 3000K Negro DALI"},
        {"cod": "MR-20W-24-3000-N",     "desc": "Micro Runner 20W 24° 3000K Negro DALI"},
        {"cod": "MR-20W-24-4000-N",     "desc": "Micro Runner 20W 24° 4000K Negro"},
        {"cod": "MR-20W-36-3000-N",     "desc": "Micro Runner 20W 36° 3000K Negro"},
        {"cod": "MR-CCT-10W-24-N",      "desc": "Micro Runner CCT 10W 24° Dinámico DALI Negro"},
    ],

    # ── RUNNER X PRO ─────────────────────────────────────────────────────────
    "RUNNER X PRO": [
        {"cod": "RXP-2W-24-3000-N",     "desc": "Runner X Pro 2W 24° 3000K Negro CRI≥90"},
        {"cod": "RXP-7W-15-2700-N",     "desc": "Runner X Pro 7W 15° 2700K Negro CRI≥90"},
        {"cod": "RXP-7W-15-3000-N",     "desc": "Runner X Pro 7W 15° 3000K Negro CRI≥90"},
        {"cod": "RXP-7W-24-3000-N",     "desc": "Runner X Pro 7W 24° 3000K Negro CRI≥90"},
        {"cod": "RXP-7W-24-3000-B",     "desc": "Runner X Pro 7W 24° 3000K Blanco CRI≥90"},
        {"cod": "RXP-15W-15-3000-N",    "desc": "Runner X Pro 15W 15° 3000K Negro DALI"},
        {"cod": "RXP-15W-24-2700-N",    "desc": "Runner X Pro 15W 24° 2700K Negro DALI"},
        {"cod": "RXP-15W-24-3000-N",    "desc": "Runner X Pro 15W 24° 3000K Negro DALI"},
        {"cod": "RXP-15W-24-3000-B",    "desc": "Runner X Pro 15W 24° 3000K Blanco DALI"},
        {"cod": "RXP-15W-36-3000-N",    "desc": "Runner X Pro 15W 36° 3000K Negro"},
        {"cod": "RXP-30W-15-3000-N",    "desc": "Runner X Pro 30W 15° 3000K Negro DALI"},
        {"cod": "RXP-30W-24-3000-N",    "desc": "Runner X Pro 30W 24° 3000K Negro DALI"},
        {"cod": "RXP-30W-24-4000-N",    "desc": "Runner X Pro 30W 24° 4000K Negro"},
        {"cod": "RXP-30W-36-3000-N",    "desc": "Runner X Pro 30W 36° 3000K Negro"},
        {"cod": "RXP-CCT-15W-24-N",     "desc": "Runner X Pro CCT 15W 24° Dinámico DALI Negro"},
        {"cod": "RXP-CCT-30W-24-N",     "desc": "Runner X Pro CCT 30W 24° Dinámico DALI Negro"},
        {"cod": "RXP-30W-24-3000-SUP",  "desc": "Runner X Pro 30W 24° 3000K aplicado superficie"},
    ],

    # ── TRACK LV ─────────────────────────────────────────────────────────────
    "TRACK LV": [
        {"cod": "TLVL-RIEL-1M-N",       "desc": "Track LV riel 48V 1m negro"},
        {"cod": "TLVL-RIEL-1M-B",       "desc": "Track LV riel 48V 1m blanco"},
        {"cod": "TLVL-RIEL-2M-N",       "desc": "Track LV riel 48V 2m negro"},
        {"cod": "TLVL-RIEL-3M-N",       "desc": "Track LV riel 48V 3m negro"},
        {"cod": "TLVL-10W-3000-N",      "desc": "Track LV proyector 10W 3000K 48V negro"},
        {"cod": "TLVL-10W-3000-B",      "desc": "Track LV proyector 10W 3000K 48V blanco"},
        {"cod": "TLVL-CON-L-N",         "desc": "Track LV conector L 48V negro"},
    ],

    # ── TRACKLIGHTS ──────────────────────────────────────────────────────────
    "TRACKLIGHTS": [
        {"cod": "TL-3W-24-2700-N",      "desc": "Tracklight 3W 24° 2700K Negro CRI≥80"},
        {"cod": "TL-3W-24-3000-N",      "desc": "Tracklight 3W 24° 3000K Negro CRI≥80"},
        {"cod": "TL-7W-15-3000-N",      "desc": "Tracklight 7W 15° 3000K Negro CRI≥90"},
        {"cod": "TL-7W-24-2700-N",      "desc": "Tracklight 7W 24° 2700K Negro CRI≥90"},
        {"cod": "TL-7W-24-3000-N",      "desc": "Tracklight 7W 24° 3000K Negro CRI≥90"},
        {"cod": "TL-7W-24-3000-B",      "desc": "Tracklight 7W 24° 3000K Blanco CRI≥90"},
        {"cod": "TL-7W-36-3000-N",      "desc": "Tracklight 7W 36° 3000K Negro CRI≥80"},
        {"cod": "TL-7W-60-4000-N",      "desc": "Tracklight 7W 60° 4000K Negro CRI≥80"},
        {"cod": "TL-15W-15-3000-N",     "desc": "Tracklight 15W 15° 3000K Negro DALI CRI≥90"},
        {"cod": "TL-15W-24-2700-N",     "desc": "Tracklight 15W 24° 2700K Negro DALI CRI≥90"},
        {"cod": "TL-15W-24-3000-N",     "desc": "Tracklight 15W 24° 3000K Negro DALI CRI≥90"},
        {"cod": "TL-15W-24-3000-B",     "desc": "Tracklight 15W 24° 3000K Blanco DALI"},
        {"cod": "TL-15W-36-4000-N",     "desc": "Tracklight 15W 36° 4000K Negro DALI"},
        {"cod": "TL-27W-15-3000-N",     "desc": "Tracklight 27W 15° 3000K Negro DALI CRI≥90"},
        {"cod": "TL-27W-24-3000-N",     "desc": "Tracklight 27W 24° 3000K Negro DALI CRI≥90"},
        {"cod": "TL-27W-24-4000-N",     "desc": "Tracklight 27W 24° 4000K Negro DALI"},
        {"cod": "TL-CCT-15W-24-N",      "desc": "Tracklight CCT 15W 24° Dinámico 1-10V Negro"},
        {"cod": "TL-CCT-27W-24-N",      "desc": "Tracklight CCT 27W 24° Dinámico 1-10V Negro"},
        {"cod": "TL-7W-24-3000-48V",    "desc": "Tracklight 7W 24° 3000K Negro 48V riel"},
        {"cod": "TL-15W-24-3000-48V",   "desc": "Tracklight 15W 24° 3000K Negro 48V riel"},
        {"cod": "TL-SUP-15W-24-3000-N", "desc": "Tracklight suspendido 15W 24° 3000K Negro"},
        {"cod": "TL-SUP-27W-15-3000-N", "desc": "Tracklight suspendido 27W 15° 3000K Negro"},
        {"cod": "TL-RIEL-1M-N",         "desc": "Riel monofásico 1m superficie negro"},
        {"cod": "TL-RIEL-2M-N",         "desc": "Riel monofásico 2m superficie negro"},
        {"cod": "TL-RIEL-3M-N",         "desc": "Riel monofásico 3m superficie negro"},
        {"cod": "TL-RIEL-EMP-1M-N",     "desc": "Riel monofásico empotrado 1m negro"},
        {"cod": "TL-RIEL-EMP-2M-N",     "desc": "Riel monofásico empotrado 2m negro"},
        {"cod": "TL-CON-T-N",           "desc": "Conector T para riel monofásico negro"},
        {"cod": "TL-CON-L-N",           "desc": "Conector L 90° para riel monofásico negro"},
        {"cod": "TL-ALIM-N",            "desc": "Alimentador extremo para riel monofásico negro"},
        {"cod": "TL-CON-F-N",           "desc": "Conector flexible para riel monofásico negro"},
    ],

    # ── MÓDULOS LED ──────────────────────────────────────────────────────────
    "MÓDULOS LED": [
        {"cod": "MOD-20W-2700-N",       "desc": "Módulo LED 20W 2700K CRI≥90"},
        {"cod": "MOD-20W-3000-N",       "desc": "Módulo LED 20W 3000K CRI≥90"},
        {"cod": "MOD-20W-4000-N",       "desc": "Módulo LED 20W 4000K CRI≥80"},
        {"cod": "MOD-30W-2700-N",       "desc": "Módulo LED 30W 2700K CRI≥90"},
        {"cod": "MOD-30W-3000-N",       "desc": "Módulo LED 30W 3000K CRI≥90"},
        {"cod": "MOD-30W-4000-N",       "desc": "Módulo LED 30W 4000K CRI≥80"},
        {"cod": "MOD-50W-3000-N",       "desc": "Módulo LED 50W 3000K CRI≥80"},
        {"cod": "MOD-50W-4000-N",       "desc": "Módulo LED 50W 4000K CRI≥80"},
        {"cod": "MOD-100W-3000-N",      "desc": "Módulo LED 100W 3000K CRI≥80"},
        {"cod": "MOD-10W-PARED-2700",   "desc": "Módulo LED pared 10W 2700K CRI≥90"},
        {"cod": "MOD-10W-PARED-3000",   "desc": "Módulo LED pared 10W 3000K CRI≥90"},
        {"cod": "MOD-20W-PARED-3000",   "desc": "Módulo LED pared 20W 3000K CRI≥80"},
        {"cod": "MOD-CCT-30W",          "desc": "Módulo LED CCT 30W Dinámico 2700K–4000K"},
    ],

    # ── WALLY ────────────────────────────────────────────────────────────────
    "WALLY": [
        {"cod": "WALLY-300-2700-N",     "desc": "Wally Aplique Lineal 300mm 2700K Negro"},
        {"cod": "WALLY-300-3000-N",     "desc": "Wally Aplique Lineal 300mm 3000K Negro"},
        {"cod": "WALLY-300-3000-B",     "desc": "Wally Aplique Lineal 300mm 3000K Blanco"},
        {"cod": "WALLY-600-2700-N",     "desc": "Wally Aplique Lineal 600mm 2700K Negro"},
        {"cod": "WALLY-600-3000-N",     "desc": "Wally Aplique Lineal 600mm 3000K Negro"},
        {"cod": "WALLY-600-3000-B",     "desc": "Wally Aplique Lineal 600mm 3000K Blanco"},
        {"cod": "WALLY-1200-2700-N",    "desc": "Wally Aplique Lineal 1200mm 2700K Negro DALI"},
        {"cod": "WALLY-1200-3000-N",    "desc": "Wally Aplique Lineal 1200mm 3000K Negro DALI"},
        {"cod": "WALLY-1200-3000-B",    "desc": "Wally Aplique Lineal 1200mm 3000K Blanco DALI"},
        {"cod": "WALLY-1800-3000-N",    "desc": "Wally Aplique Lineal 1800mm 3000K Negro DALI"},
        {"cod": "WALLY-1800-2700-N",    "desc": "Wally Aplique Lineal 1800mm 2700K Negro DALI"},
        {"cod": "WALLY-CCT-600-N",      "desc": "Wally Aplique Lineal CCT 600mm Dinámico DALI Negro"},
        {"cod": "WALLY-CCT-1200-N",     "desc": "Wally Aplique Lineal CCT 1200mm Dinámico DALI Negro"},
        {"cod": "WALLY-CCT-1800-N",     "desc": "Wally Aplique Lineal CCT 1800mm Dinámico DALI Negro"},
    ],

    # ── LINEAR ───────────────────────────────────────────────────────────────
    "LINEAR": [
        {"cod": "LINEAR-300-2700-N",    "desc": "Linear Bañador Lineal 300mm 2700K Negro"},
        {"cod": "LINEAR-300-3000-N",    "desc": "Linear Bañador Lineal 300mm 3000K Negro"},
        {"cod": "LINEAR-300-3000-B",    "desc": "Linear Bañador Lineal 300mm 3000K Blanco"},
        {"cod": "LINEAR-600-2700-N",    "desc": "Linear Bañador Lineal 600mm 2700K Negro"},
        {"cod": "LINEAR-600-3000-N",    "desc": "Linear Bañador Lineal 600mm 3000K Negro"},
        {"cod": "LINEAR-600-3000-B",    "desc": "Linear Bañador Lineal 600mm 3000K Blanco"},
        {"cod": "LINEAR-1200-2700-N",   "desc": "Linear Bañador Lineal 1200mm 2700K Negro DALI"},
        {"cod": "LINEAR-1200-3000-N",   "desc": "Linear Bañador Lineal 1200mm 3000K Negro DALI"},
        {"cod": "LINEAR-1200-3000-B",   "desc": "Linear Bañador Lineal 1200mm 3000K Blanco DALI"},
        {"cod": "LINEAR-1800-3000-N",   "desc": "Linear Bañador Lineal 1800mm 3000K Negro DALI"},
        {"cod": "LINEAR-1800-2700-N",   "desc": "Linear Bañador Lineal 1800mm 2700K Negro DALI"},
        {"cod": "LINEAR-CCT-1200-N",    "desc": "Linear Bañador CCT 1200mm Dinámico DALI Negro"},
        {"cod": "LINEAR-CCT-1800-N",    "desc": "Linear Bañador CCT 1800mm Dinámico DALI Negro"},
        {"cod": "LINEAR-EMP-600-3000-N","desc": "Linear Bañador empotrado 600mm 3000K Negro"},
    ],

    # ── EXTERIOR ─────────────────────────────────────────────────────────────
    "EXTERIOR": [
        {"cod": "EXT-SPOT-3W-3000-N",   "desc": "Spot exterior empotrado piso 3W 3000K IP65 Negro"},
        {"cod": "EXT-SPOT-5W-3000-N",   "desc": "Spot exterior empotrado piso 5W 3000K IP65 Negro"},
        {"cod": "EXT-SPOT-10W-2700-N",  "desc": "Spot exterior empotrado piso 10W 2700K IP65 Negro"},
        {"cod": "EXT-SPOT-10W-3000-N",  "desc": "Spot exterior empotrado piso 10W 3000K IP65 Negro"},
        {"cod": "EXT-APL-10W-3000-N",   "desc": "Aplique exterior pared 10W 3000K IP65 Negro"},
        {"cod": "EXT-APL-10W-4000-N",   "desc": "Aplique exterior pared 10W 4000K IP65 Negro"},
        {"cod": "EXT-APL-20W-3000-N",   "desc": "Aplique exterior pared 20W 3000K IP65 Negro"},
        {"cod": "EXT-APL-20W-4000-N",   "desc": "Aplique exterior pared 20W 4000K IP65 Negro"},
        {"cod": "EXT-PROY-30W-3000-N",  "desc": "Proyector exterior 30W 3000K IP65 Negro"},
        {"cod": "EXT-PROY-30W-4000-N",  "desc": "Proyector exterior 30W 4000K IP65 Negro"},
        {"cod": "EXT-PROY-50W-3000-N",  "desc": "Proyector exterior 50W 3000K IP65 Negro"},
        {"cod": "EXT-PROY-50W-4000-N",  "desc": "Proyector exterior 50W 4000K IP65 Negro"},
    ],

    # ── SISTEMAS CONTROL ─────────────────────────────────────────────────────
    "SISTEMAS CONTROL": [
        {"cod": "SC-TRIAC-1CH-220V",    "desc": "Controlador TRIAC 1 canal 220V 400W"},
        {"cod": "SC-TRIAC-4CH-220V",    "desc": "Controlador TRIAC 4 canales 220V"},
        {"cod": "SC-110V-4CH-DALI",     "desc": "Controlador DALI 4 canales 220V bus externo"},
        {"cod": "SC-DALI-GW-IP20",      "desc": "Gateway DALI IP20 64 direcciones"},
        {"cod": "SC-DALI-GW-IP44",      "desc": "Gateway DALI IP44 64 direcciones"},
        {"cod": "SC-DMX-1-10V",         "desc": "Controlador DMX a 1-10V 8 canales"},
        {"cod": "SC-WIFI-TOUCH",        "desc": "Panel táctil WiFi regulación escenas"},
        {"cod": "SC-CASAMBI-MOD",       "desc": "Módulo Casambi para integración inalámbrica"},
        {"cod": "SC-SENSOR-MOV",        "desc": "Sensor de movimiento IR para DALI"},
        {"cod": "SC-SENSOR-LUX",        "desc": "Sensor de luminosidad para DALI"},
    ],
}


class Command(BaseCommand):
    help = 'Populate Producto table from PRODUCTOS dict (idempotent via update_or_create)'

    def handle(self, *args, **options):
        updated = 0
        created = 0
        skipped = 0
        for nombre, productos in PRODUCTOS.items():
            try:
                fam = FamiliaProducto.objects.get(nombre=nombre)
                for i, p in enumerate(productos):
                    obj, was_created = Producto.objects.update_or_create(
                        codigo=p['cod'],
                        defaults={
                            'familia': fam,
                            'descripcion': p['desc'],
                            'orden': i,
                            'activo': True,
                        }
                    )
                    if was_created:
                        created += 1
                    else:
                        updated += 1
                self.stdout.write(self.style.SUCCESS(
                    f'  {nombre}: {len(productos)} productos procesados'
                ))
            except FamiliaProducto.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f'  {nombre}: familia no encontrada en DB — omitida'
                ))
                skipped += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nListo: {created} creados, {updated} actualizados, {skipped} familias omitidas.'
        ))
