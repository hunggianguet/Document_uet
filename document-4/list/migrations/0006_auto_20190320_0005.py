# Generated by Django 2.1.4 on 2019-03-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_student_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pdf',
            field=models.FileField(upload_to='media'),
        ),
    ]