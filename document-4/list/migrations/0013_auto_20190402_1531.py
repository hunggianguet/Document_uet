# Generated by Django 2.1.4 on 2019-04-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0012_auto_20190401_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='topic_type',
            field=models.CharField(choices=[('KLTN', 'Khóa luận tốt nghiệp'), ('NCKH', 'Nghiên cứu khoa học')], max_length=4, null=True),
        ),
    ]
