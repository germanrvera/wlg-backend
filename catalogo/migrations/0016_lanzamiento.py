from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0015_recursodescargable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lanzamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, help_text='Override del nombre. Si vacío, usa el nombre de familia/producto.', max_length=120)),
                ('subtitulo', models.CharField(blank=True, help_text='Override del tipo. Si vacío, usa el tipo de familia/producto.', max_length=120)),
                ('familia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lanzamientos', to='catalogo.familiaproducto', verbose_name='Familia')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lanzamientos', to='catalogo.producto', verbose_name='Producto')),
                ('imagen', models.ImageField(blank=True, upload_to='lanzamientos/')),
                ('photo', models.URLField(blank=True, help_text='URL externa (tiene prioridad sobre imagen subida).')),
                ('orden', models.PositiveSmallIntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Lanzamiento',
                'verbose_name_plural': 'Lanzamientos',
                'ordering': ['orden'],
            },
        ),
    ]
