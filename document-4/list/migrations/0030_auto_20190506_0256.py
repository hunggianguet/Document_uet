# Generated by Django 2.1.7 on 2019-05-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0029_auto_20190506_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='topic',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]