# Generated by Django 4.2 on 2023-06-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_review_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cateringbook',
            name='event_date',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cateringbook',
            name='event_time',
            field=models.TimeField(auto_created=True, blank=True, null=True),
        ),
    ]
