# Generated by Django 2.2.28 on 2024-03-21 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BrewReview', '0019_auto_20240320_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeshop',
            name='owner_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]