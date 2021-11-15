# Generated by Django 3.2.7 on 2021-11-13 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_restaurant_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodredistributor",
            name="about",
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="restaurant",
            name="about",
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
