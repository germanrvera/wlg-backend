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
    # Crawlers
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    path('llms.txt', TemplateView.as_view(template_name='llms.txt', content_type='text/plain')),
    # Site pages
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('familias/<slug:slug>', TemplateView.as_view(template_name='familia.html'), name='familia-detail'),
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
