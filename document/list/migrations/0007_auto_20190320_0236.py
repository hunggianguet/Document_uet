# Generated by Django 2.1.4 on 2019-03-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0006_auto_20190320_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
