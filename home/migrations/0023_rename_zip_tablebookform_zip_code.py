# Generated by Django 4.2 on 2023-06-08 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_placesnearby_date_field_placesnearby_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablebookform',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
