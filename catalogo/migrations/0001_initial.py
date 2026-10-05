from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='familias/')),
                ('tipo', models.CharField(max_length=60)),
                ('orden', models.PositiveSmallIntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Familia de Producto',
                'verbose_name_plural': 'Familias de Productos',
                'ordering': ['orden', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.CharField(max_length=120)),
                ('año', models.PositiveSmallIntegerField()),
                ('tipo_espacio', models.CharField(max_length=80)),
                ('imagen_principal', models.ImageField(upload_to='proyectos/')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['-año', '-creado'],
            },
        ),
    ]
