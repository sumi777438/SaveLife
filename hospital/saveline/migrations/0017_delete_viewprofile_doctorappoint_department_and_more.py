# Generated by Django 4.1.4 on 2022-12-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveline', '0016_doctorappoint_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ViewProfile',
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='department',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='designation',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='education',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='hospital',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='research',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='specialization_area',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctorappoint',
            name='training',
            field=models.TextField(max_length=500, null=True),
        ),
    ]