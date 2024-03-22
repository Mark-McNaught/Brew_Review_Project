from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from BrewReview.models import CoffeeShop
from django.contrib.admin.sites import AdminSite
from BrewReview.admin import CoffeeShopAdmin
from BrewReview.apps import BrewreviewConfig
from BrewReview.forms import CoffeeShopForm, ReviewForm, ChangeUsernameForm
from BrewReview.models import CoffeeShop, Review
from BrewReview import views




class CoffeeShopAdminTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_superuser('admin', 'admin@test.com', 'password')
        self.client.login(username='admin', password='password')

        # Create a CoffeeShop instance
        self.coffee_shop = CoffeeShop.objects.create(
            name="Test Coffee",
            address_line_1="123 Test St",
            postcode="TST123",
            city="Testville",
            country="Testland",
            rating=4,
            price="$"
        )



        # Check if all fields in `list_display` are in the response
        self.assertContains(response, "Test Coffee")
        self.assertContains(response, "123 Test St")
        self.assertContains(response, "TST123")
        self.assertContains(response, "Testville")
        self.assertContains(response, "Testland")
        self.assertContains(response, "4")
        self.assertContains(response, "$")



class BrewreviewConfigTest(TestCase):
    def test_app_name(self):
        self.assertEqual(BrewreviewConfig.name, 'BrewReview')

class CoffeeShopFormTest(TestCase):

    def test_form_fields(self):
        form = CoffeeShopForm()
        self.assertTrue(form.fields['name'].max_length == 128)
        self.assertTrue(form.fields['description'].max_length == 1000)
        self.assertFalse(form.fields['serves_food'].required)
        self.assertIsInstance(form.fields['price'].choices, list)
        self.assertTrue(form.fields['address_line_1'].max_length == 128)
        self.assertTrue(form.fields['postcode'].max_length == 10)
        self.assertTrue(form.fields['city'].max_length == 128)
        self.assertTrue(form.fields['country'].max_length == 128)
        self.assertFalse(form.fields['picture'].required)

    def test_form_validity(self):
        form_data = {
            'name': 'Test Coffee',
            'description': 'A test coffee shop',
            'serves_food': True,
            'price': '3',
            'address_line_1': '123 Test Street',
            'postcode': 'TEST123',
            'city': 'Test City',
            'country': 'Test Country',
        }
        form = CoffeeShopForm(data=form_data)
        self.assertTrue(form.is_valid())

class ReviewFormTest(TestCase):

    def test_form_fields(self):
        form = ReviewForm()
        self.assertTrue(form.fields['title'].max_length == Review.TITLE_MAX_LENGTH)
        self.assertIsInstance(form.fields['rating'].choices, list)
        self.assertTrue(form.fields['review'].max_length == Review.REVIEW_MAX_LENGTH)

    def test_form_validity(self):
        form_data = {
            'title': 'Test Review',
            'rating': '5',
            'review': 'This is a test review for a coffee shop.',
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

class ChangeUsernameFormTest(TestCase):

    def test_form_fields(self):
        form = ChangeUsernameForm()
        self.assertTrue(form.fields['new_username'].max_length == 150)

    def test_form_validity(self):
        form_data = {'new_username': 'newuser123'}
        form = ChangeUsernameForm(data=form_data)
        self.assertTrue(form.is_valid())

class CoffeeShopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        CoffeeShop.objects.create(
            owner_id=user,
            name='Test Coffee Shop',
            description='A test description',
            address_line_1='123 Test Street',
            postcode='TEST123',
            city='Test City',
            country='Test Country'
        )


class ReviewModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='reviewuser')
        coffee_shop = CoffeeShop.objects.create(name='Test Coffee for Review')
        Review.objects.create(
            coffee_shop=coffee_shop,
            user=user,
            title='Test Review',
            rating=5,
            review='This is a test review'
        )

    def test_review_creation(self):
        review = Review.objects.get(id=1)
        self.assertEqual(review.title, 'Test Review')
        self.assertEqual(review.rating, 5)


class URLTests(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('BrewReview:index')
        self.assertEqual(resolve(url).func, views.index)

    def test_map_url_resolves(self):
        url = reverse('BrewReview:map')
        self.assertEqual(resolve(url).func, views.map)

    def test_shops_url_resolves(self):
        url = reverse('BrewReview:shops')
        self.assertEqual(resolve(url).func, views.shops)

    def test_show_shop_url_resolves(self):
        url = reverse('BrewReview:show_shop', kwargs={'shop_slug': 'some-shop'})
        self.assertEqual(resolve(url).func, views.show_shop)

    def test_add_shop_url_resolves(self):
        url = reverse('BrewReview:add_shop')
        self.assertEqual(resolve(url).func, views.add_shop)

    def test_add_review_url_resolves(self):
        url = reverse('BrewReview:add_review', kwargs={'shop_slug': 'some-shop'})
        self.assertEqual(resolve(url).func, views.add_review)

    def test_searched_url_resolves(self):
        url = reverse('BrewReview:searched')
        self.assertEqual(resolve(url).func, views.searched)

    def test_profile_url_resolves(self):
        url = reverse('BrewReview:profile')
        self.assertEqual(resolve(url).func, views.profile)

    def test_account_settings_url_resolves(self):
        url = reverse('BrewReview:account_settings')
        self.assertEqual(resolve(url).func, views.account_settings)

    def test_change_username_url_resolves(self):
        url = reverse('BrewReview:change_username')
        self.assertEqual(resolve(url).func, views.change_username)

    def test_delete_account_url_resolves(self):
        url = reverse('BrewReview:delete_account')
        self.assertEqual(resolve(url).func, views.delete_account)
