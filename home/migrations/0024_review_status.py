# Generated by Django 4.2 on 2023-06-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_rename_zip_tablebookform_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('inactive', 'inactive')], max_length=100, null=True),
        ),
    ]
