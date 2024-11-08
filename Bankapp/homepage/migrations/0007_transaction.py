# Generated by Django 5.1.2 on 2024-10-24 07:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_accountholder_gender_accountholder_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('debit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('accountno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.accountholder')),
            ],
        ),
    ]
