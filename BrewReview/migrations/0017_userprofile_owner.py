# Generated by Django 2.2.28 on 2024-03-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrewReview', '0016_auto_20240317_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='owner',
            field=models.BooleanField(default=False),
        ),
    ]
