# Generated by Django 2.2.7 on 2020-06-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200623_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacion',
            name='ruta_imagen',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
