# Generated by Django 5.0.6 on 2025-01-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0035_last_replay_data_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='last_replay_data',
            name='last_count',
            field=models.CharField(default=0, max_length=3),
        ),
    ]
