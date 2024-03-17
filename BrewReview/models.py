from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class CoffeeShop(models.Model):
    # Table for storing details about a coffee shop
    NAME_MAX_LENGTH = 128
    DESC_MAX_LENGTH = 1000
    ADDRESS_MAX_LENGTH = 256
    POSTCODE_MAX_LENGTH = 10

    shop_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=DESC_MAX_LENGTH, default='')

    address_line_1 = models.CharField(max_length=ADDRESS_MAX_LENGTH, default='')
    postcode = models.CharField(max_length=POSTCODE_MAX_LENGTH, default='')
    city = models.CharField(max_length=ADDRESS_MAX_LENGTH, null = True, default='')
    country = models.CharField(max_length=ADDRESS_MAX_LENGTH, default='')

    lat = models.FloatField(default=None, null=True,)
    lng = models.FloatField(default=None, null=True)

    # Need to implement image folder still
    image_location_folder = models.URLField(max_length=256, unique=True, null=True)

    serves_food = models.BooleanField(default=False)

    # Need to implement average rating still
    rating = models.IntegerField(default=0, null=True)

    price = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CoffeeShop, self).save(*args, **kwargs)



class Review(models.Model):
    # Table for storing details about a coffee shop review
    TITLE_MAX_LENGTH = 256
    REVIEW_MAX_LENGTH = 1000

    review_id = models.AutoField(primary_key=True)
    coffee_shop = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    rating = models.IntegerField(default=0)
    review = models.TextField(max_length=REVIEW_MAX_LENGTH)

    def __str__(self):
        return str(self.review_id)


class SavedReviews(models.Model):
    # Table that stores refernces to users and their saved reviews
    save_id = models.AutoField(primary_key=True)
    review_id = models.ManyToManyField(Review)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = 'SavedReviews'

    def __str__(self):
        return str(self.save_id)


class FavouriteShops(models.Model):
    # Table that stores refernces to users and their favourited coffee shops
    fav_id = models.AutoField(primary_key=True)
    shop_id = models.ManyToManyField(CoffeeShop)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = 'FavouriteShops'

    def __str__(self):
        return str(self.fav_id)





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    owner = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username