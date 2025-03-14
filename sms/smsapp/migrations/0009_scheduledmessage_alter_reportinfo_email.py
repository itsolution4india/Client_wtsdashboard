# Generated by Django 5.0.6 on 2024-09-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0008_registerapp_customuser_register_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.CharField(max_length=50)),
                ('template_name', models.CharField(max_length=255)),
                ('media_id', models.CharField(blank=True, max_length=255, null=True)),
                ('all_contact', models.TextField()),
                ('contact_list', models.TextField()),
                ('campaign_title', models.CharField(max_length=255)),
                ('schedule_date', models.CharField(max_length=50)),
                ('schedule_time', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='reportinfo',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
