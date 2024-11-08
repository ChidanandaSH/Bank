# Generated by Django 5.1.2 on 2024-11-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_billpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountholder',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]