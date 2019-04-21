# Generated by Django 2.1.8 on 2019-04-03 15:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_auto_20190402_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='academic_year',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='reviewer',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tutor',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='work_unit',
            field=models.CharField(max_length=300, null=True),
        ),
    ]