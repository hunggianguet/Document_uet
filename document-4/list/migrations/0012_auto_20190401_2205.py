# Generated by Django 2.1.4 on 2019-04-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0011_student_topic_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='kltn',
        ),
        migrations.RemoveField(
            model_name='student',
            name='nckh',
        ),
    ]
