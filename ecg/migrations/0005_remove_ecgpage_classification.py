# Generated by Django 4.2.9 on 2024-05-05 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecg', '0004_ecgpage_classification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecgpage',
            name='classification',
        ),
    ]
