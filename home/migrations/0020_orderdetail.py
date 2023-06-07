# Generated by Django 4.2 on 2023-06-05 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_eventbook_rename_bookingform_cateringbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=True, max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('qty', models.PositiveIntegerField(default=True)),
                ('price', models.IntegerField()),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]