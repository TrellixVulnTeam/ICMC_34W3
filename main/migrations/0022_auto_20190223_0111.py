# Generated by Django 2.1.7 on 2019-02-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20190223_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='first_name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='last_name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
