# Generated by Django 2.2.7 on 2020-06-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20200628_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacion',
            name='ruta_imagen',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
