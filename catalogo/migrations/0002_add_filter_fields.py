from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiaproducto',
            name='photo',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='macro',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='skus',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_ct',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_ip',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_dim_sys',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_cri',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_v',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_w',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_ubicacion',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_aplicacion',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='filter_montaje',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='has_dim',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='w_range',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='familiaproducto',
            name='productos',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='familiaproducto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='familias/'),
        ),
    ]
