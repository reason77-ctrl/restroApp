# Generated by Django 4.2 on 2023-06-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_cateringbook_event_date_cateringbook_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cateringbook',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]