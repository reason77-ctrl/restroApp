# Generated by Django 4.2 on 2023-06-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_cart_price_alter_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=150)),
                ('date_field', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='BookingForm',
            new_name='CateringBook',
        ),
    ]
