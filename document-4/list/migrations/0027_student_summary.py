# Generated by Django 2.1.7 on 2019-05-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0026_auto_20190505_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='summary',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
