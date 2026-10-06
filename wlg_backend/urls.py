from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from catalogo.views_test import health_check

urlpatterns = [
    path('health/', health_check, name='health'),
    path('admin/', admin.site.urls),
    path('api/', include('catalogo.urls')),
    # Site pages
    path('', TemplateView.as_view(template_name='wlg_v8.html'), name='home'),
    path('familias', TemplateView.as_view(template_name='familias.html'), name='familias'),
    path('proyectos', TemplateView.as_view(template_name='proyectos.html'), name='proyectos'),
    path('contacto', TemplateView.as_view(template_name='contactar.html'), name='contacto'),
    path('recursos', TemplateView.as_view(template_name='recursos.html'), name='recursos'),
    path('experiencia', TemplateView.as_view(template_name='experiencia.html'), name='experiencia'),
    path('proyecto', TemplateView.as_view(template_name='proyecto.html'), name='proyecto'),
    path('novedades', TemplateView.as_view(template_name='novedades.html'), name='novedades'),
    path('historia', TemplateView.as_view(template_name='historia.html'), name='historia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
