# Generated by Django 3.0.6 on 2020-09-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='doing',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='kinds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='members',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='place',
            field=models.IntegerField(default=0),
        ),
    ]
