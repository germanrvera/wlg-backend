from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0014_load_distribuidores'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoDescargable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ej: Galuy — Fotometría 3000K 30°', max_length=200)),
                ('familia', models.CharField(help_text='Nombre de la familia. Usar "General" para catálogos y guías.', max_length=120)),
                ('tipo', models.CharField(choices=[('IES', 'IES / Fotometría'), ('CAD', 'CAD / DWG'), ('PDF', 'PDF / Ficha técnica'), ('BIM', 'BIM / Revit')], max_length=10)),
                ('tamano', models.CharField(blank=True, help_text='Ej: 2.4 MB', max_length=20)),
                ('archivo', models.FileField(blank=True, help_text='Se sube a R2 automáticamente.', upload_to='recursos/')),
                ('url_externa', models.URLField(blank=True, help_text='URL directa (tiene prioridad sobre el archivo subido).')),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Recurso descargable',
                'verbose_name_plural': 'Recursos descargables',
                'ordering': ['familia', 'tipo', 'orden', 'nombre'],
            },
        ),
    ]
