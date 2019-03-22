# Generated by Django 2.1.7 on 2019-03-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_notification_watched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='status',
            field=models.CharField(choices=[('wait', 'wait'), ('look', 'look'), ('rejected', 'rejected'), ('payment', 'waiting for payment'), ('accepted', 'accepted')], default='wait', max_length=100),
        ),
    ]
