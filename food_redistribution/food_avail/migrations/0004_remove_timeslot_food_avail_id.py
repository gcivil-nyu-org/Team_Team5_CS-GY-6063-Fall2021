# Generated by Django 3.2.7 on 2021-11-18 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_avail', '0003_timeslot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='food_avail_id',
        ),
    ]
