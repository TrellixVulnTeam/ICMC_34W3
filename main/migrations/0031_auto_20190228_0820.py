# Generated by Django 2.1.7 on 2019-02-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20190228_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]