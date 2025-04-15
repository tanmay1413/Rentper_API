# Generated by Django 5.2 on 2025-04-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailed_hotel_info', models.TextField(max_length=3000)),
                ('cancellation_policy', models.TextField(max_length=3000)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('pet_policy', models.TextField(blank=True, max_length=2000, null=True)),
                ('check_in_time', models.TimeField()),
                ('check_out_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
