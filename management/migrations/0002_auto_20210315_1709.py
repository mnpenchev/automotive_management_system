# Generated by Django 3.1.6 on 2021-03-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='currently_available',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='derivative',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
