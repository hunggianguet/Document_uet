# Generated by Django 2.1.4 on 2019-03-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='grade',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='reviewer',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='stt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='topic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='tutor',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
