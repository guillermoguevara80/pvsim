# Generated by Django 2.2.7 on 2020-06-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200623_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacion',
            name='ruta_imagen',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
