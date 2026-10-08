from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_load_familias'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(help_text='Etiqueta pequeña encima del título', max_length=60)),
                ('titulo', models.CharField(help_text='Título principal (\\n para salto de línea)', max_length=120)),
                ('descripcion', models.CharField(max_length=300)),
                ('cta_texto', models.CharField(default='Descubrir', max_length=60)),
                ('cta_url', models.CharField(default='/familias', max_length=200)),
                ('imagen', models.ImageField(blank=True, upload_to='hero/')),
                ('photo', models.URLField(blank=True, help_text='URL externa (tiene prioridad sobre imagen subida)')),
                ('alt', models.CharField(blank=True, max_length=120)),
                ('orden', models.PositiveSmallIntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Slide Hero',
                'verbose_name_plural': 'Slides Hero',
                'ordering': ['orden'],
            },
        ),
    ]
