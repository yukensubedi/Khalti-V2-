# Generated by Django 4.1.5 on 2023-02-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_rename_pidx_verification'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.JSONField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='verification',
            options={'verbose_name': 'verification', 'verbose_name_plural': 'verification'},
        ),
    ]
