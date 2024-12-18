# Generated by Django 5.1.2 on 2024-10-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('accountno', models.IntegerField(max_length=11)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('mobileno', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='Holder_images/')),
                ('branch', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('initialdeposit', models.FloatField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
