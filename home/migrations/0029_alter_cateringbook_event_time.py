# Generated by Django 4.2 on 2023-06-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_remove_cateringbook_event_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cateringbook',
            name='event_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
