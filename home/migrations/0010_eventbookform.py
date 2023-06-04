# Generated by Django 4.2 on 2023-05-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_imageslider_date_field_imageslider_slider_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventBookForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=50)),
                ('date_field', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
