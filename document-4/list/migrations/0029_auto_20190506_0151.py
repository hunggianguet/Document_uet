# Generated by Django 2.1.7 on 2019-05-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0028_auto_20190506_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_year',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_student',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='reviewer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='summary',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='topic_type',
            field=models.CharField(blank=True, choices=[('KLTN', 'Khóa luận tốt nghiệp'), ('NCKH', 'Nghiên cứu khoa học')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tutor',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='work_unit',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]