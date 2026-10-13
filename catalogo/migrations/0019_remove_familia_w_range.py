from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0018_clear_wlg_filter_aplicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiaproducto',
            name='w_range',
        ),
    ]
