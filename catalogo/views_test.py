from django.http import JsonResponse


def health_check(request):
    """Simple health check endpoint"""
    return JsonResponse({
        'status': 'ok',
        'message': 'Django is running',
        'debug': __import__('django.conf', fromlist=['settings']).settings.DEBUG,
    })
