# Generated by Django 2.1.7 on 2019-04-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_auto_20190403_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrequest',
            name='payed',
            field=models.BooleanField(default=False),
        ),
    ]