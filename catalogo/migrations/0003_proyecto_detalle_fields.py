from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_add_filter_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='lead',
            field=models.TextField(blank=True, help_text='Párrafo introductorio largo'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='quote',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='quote_autor',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='galeria',
            field=models.JSONField(default=list, help_text='Lista de URLs de imágenes de la galería'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='bloques',
            field=models.JSONField(default=list, help_text='Lista de {num, title, img, text}'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='ficha_tecnica',
            field=models.JSONField(default=dict, help_text='Dict de {clave: valor}'),
        ),
    ]
