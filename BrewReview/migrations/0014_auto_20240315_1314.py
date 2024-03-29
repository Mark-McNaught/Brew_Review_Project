# Generated by Django 2.2.28 on 2024-03-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrewReview', '0013_auto_20240313_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffeeshop',
            name='address',
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='address_line_1',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='city',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='country',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coffeeshop',
            name='postcode',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
