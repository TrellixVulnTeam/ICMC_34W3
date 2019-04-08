# Generated by Django 2.1.7 on 2019-04-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_auto_20190406_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine',
            name='boat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Boat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fine',
            name='reason',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
