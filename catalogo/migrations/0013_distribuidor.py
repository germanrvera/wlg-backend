from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_load_configuracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('ciudad', models.CharField(max_length=80)),
                ('zona', models.CharField(max_length=80, help_text='Provincia o región (para búsqueda)')),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=40)),
                ('url_mapa', models.URLField(blank=True, help_text='URL de Google Maps')),
                ('tipo', models.CharField(
                    choices=[('Oficial', 'Oficial'), ('Autorizado', 'Autorizado')],
                    default='Autorizado', max_length=20
                )),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Distribuidor',
                'verbose_name_plural': 'Distribuidores',
                'ordering': ['zona', 'ciudad', 'orden', 'nombre'],
            },
        ),
    ]
