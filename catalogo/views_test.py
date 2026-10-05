from django.http import JsonResponse
from catalogo.models import FamiliaProducto, Proyecto


def health_check(request):
    """Simple health check endpoint"""
    try:
        familia_count = FamiliaProducto.objects.count()
        proyecto_count = Proyecto.objects.count()
        return JsonResponse({
            'status': 'ok',
            'message': 'Django is running',
            'debug': __import__('django.conf', fromlist=['settings']).settings.DEBUG,
            'db_familias': familia_count,
            'db_proyectos': proyecto_count,
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
            'error_type': type(e).__name__,
        }, status=500)
