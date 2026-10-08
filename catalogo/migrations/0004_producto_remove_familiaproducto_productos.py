from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_proyecto_detalle_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=80, unique=True, verbose_name='Código SKU')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripción')),
                ('imagen', models.ImageField(blank=True, upload_to='productos/', verbose_name='Imagen')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio (ARS)')),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.PositiveSmallIntegerField(default=0)),
                ('familia', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='items',
                    to='catalogo.familiaproducto',
                    verbose_name='Familia'
                )),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['familia__orden', 'orden', 'codigo'],
            },
        ),
        migrations.RemoveField(
            model_name='familiaproducto',
            name='productos',
        ),
    ]
