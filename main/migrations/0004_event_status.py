# Generated by Django 4.0.1 on 2022-08-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
