# Generated by Django 4.2 on 2023-05-22 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_booking_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_US',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='booking_form',
            name='date_field',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
