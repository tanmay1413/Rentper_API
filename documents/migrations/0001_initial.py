# Generated by Django 5.2 on 2025-04-15 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0002_remove_specialservice_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_number', models.CharField(max_length=100)),
                ('pan_card', models.FileField(blank=True, null=True, upload_to='documents/pan_cards/')),
                ('hotel_license', models.FileField(blank=True, null=True, upload_to='documents/hotel_licenses/')),
                ('hotel_ownership_proof', models.FileField(blank=True, null=True, upload_to='documents/ownership_proofs/')),
                ('fssai_license', models.FileField(blank=True, null=True, upload_to='documents/fssai_licenses/')),
                ('fire_safety_certificate', models.FileField(blank=True, null=True, upload_to='documents/fire_safety_certificates/')),
                ('owner_identity_proof', models.FileField(blank=True, null=True, upload_to='documents/owner_ids/')),
                ('manager_identity_proof', models.FileField(blank=True, null=True, upload_to='documents/manager_ids/')),
                ('authorization_letter', models.FileField(blank=True, null=True, upload_to='documents/authorization_letters/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='legal_documents', to='hotels.hotel')),
            ],
        ),
    ]
