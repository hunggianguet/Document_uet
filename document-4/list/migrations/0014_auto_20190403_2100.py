# Generated by Django 2.1.4 on 2019-04-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_auto_20190402_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
