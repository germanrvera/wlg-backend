from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_producto_remove_familiaproducto_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
    ]
