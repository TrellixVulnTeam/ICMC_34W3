# Generated by Django 2.1.7 on 2019-04-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0077_techcheckrequest_inspecting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('tech_check_payment_accepted', 'tech check payment accepted'), ('tech_check_payment_rejected', 'tech check payment rejected'), ('wait', 'wait'), ('look', 'look'), ('rejected', 'rejected'), ('payment', 'waiting for payment'), ('payment_check', 'waiting for payment check'), ('payment_rejected', 'payment rejected'), ('inspector_check', 'waiting for data check'), ('accepted', 'accepted')], max_length=250),
        ),
    ]