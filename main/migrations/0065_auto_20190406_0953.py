# Generated by Django 2.1.7 on 2019-04-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_auto_20190406_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='prev_numbers_or_name',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Прежние регистр. No и название судна'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='prev_registration_place',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Место прежней регистрации судна'),
        ),
    ]
