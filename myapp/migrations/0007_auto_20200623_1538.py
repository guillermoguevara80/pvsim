# Generated by Django 2.2.7 on 2020-06-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200623_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacion',
            name='ruta_imagen',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name=models.FileField(default='fig<built-in function id>.png', upload_to='media/')),
        ),
    ]