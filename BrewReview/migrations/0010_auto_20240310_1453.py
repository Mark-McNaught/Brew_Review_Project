# Generated by Django 2.2.28 on 2024-03-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrewReview', '0009_auto_20240310_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeshop',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
