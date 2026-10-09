from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_update_hero_slides_cta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.SlugField(max_length=80, unique=True, help_text='Identificador interno. No cambiar.')),
                ('valor', models.TextField(help_text='Texto visible. Podés usar <em>, <br> y <strong>.')),
                ('descripcion', models.CharField(blank=True, max_length=200, help_text='Dónde aparece este texto en el sitio.')),
                ('pagina', models.CharField(
                    choices=[
                        ('home', 'Home'), ('familias', 'Familias'), ('proyectos', 'Proyectos'),
                        ('contacto', 'Contacto'), ('recursos', 'Recursos'),
                        ('novedades', 'Novedades'), ('global', 'Global'),
                    ],
                    default='home', max_length=20
                )),
            ],
            options={
                'verbose_name': 'Configuración de texto',
                'verbose_name_plural': 'Configuración de textos',
                'ordering': ['pagina', 'clave'],
            },
        ),
    ]
