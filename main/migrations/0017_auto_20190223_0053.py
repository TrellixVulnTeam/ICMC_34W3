# Generated by Django 2.1.7 on 2019-02-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190223_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='last_name',
        ),
        migrations.AddField(
            model_name='owner',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]