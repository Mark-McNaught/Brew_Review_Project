# Generated by Django 2.2.28 on 2024-03-06 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BrewReview', '0006_auto_20240306_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresses',
            old_name='post_code',
            new_name='postcode',
        ),
    ]
