# Generated by Django 4.2 on 2023-05-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_item_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
    ]
