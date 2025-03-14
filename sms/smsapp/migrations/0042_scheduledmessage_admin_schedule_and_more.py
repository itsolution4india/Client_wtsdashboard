# Generated by Django 5.0.6 on 2025-02-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0041_contact_user_group_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledmessage',
            name='admin_schedule',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scheduledmessage',
            name='schedule_type',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Once', 'Once')], default='Once', max_length=5),
        ),
    ]
