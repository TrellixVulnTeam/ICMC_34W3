# Generated by Django 2.1.7 on 2019-03-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_removerequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boat',
            old_name='status',
            new_name='_status',
        ),
    ]
