# Generated by Django 2.2.7 on 2020-06-24 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200623_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacion',
            name='ruta_imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]