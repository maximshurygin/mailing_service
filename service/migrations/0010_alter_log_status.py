# Generated by Django 4.2.5 on 2023-09-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_remove_newsletter_send_time_newsletter_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
    ]