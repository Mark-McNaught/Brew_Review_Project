# Generated by Django 2.2.28 on 2024-03-10 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BrewReview', '0008_auto_20240308_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffeeshop',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='lat',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='lng',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='coffeeshop',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='BrewReview.Addresses'),
        ),
        migrations.AlterField(
            model_name='coffeeshop',
            name='image_location_folder',
            field=models.URLField(max_length=256, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='coffeeshop',
            name='rating',
            field=models.IntegerField(default=0, null=True),
        ),
    ]