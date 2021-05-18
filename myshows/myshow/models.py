from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Count
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# from languages.fields import LanguageField

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title





class Movie(models.Model):
    movie_type = models.CharField(max_length=100, null=True)
    movie_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    movie_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=600, null=True)

    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('moviedetails', kwargs={"id": self.id})


    # def get_absolute_url(self):
    #     return reverse('myshows/moviedetails', kwargs={"slug": self.slug})

    def countreview(self):
        reviews = Review.objects.filter(movie=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class Theatre(models.Model):
    theatre_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    ticket_price = models.CharField(max_length=100)
    sitting_type = models.CharField(max_length=100)

    def __str__(self):
        return self.theatre_name


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)
    order_id = models.CharField(max_length=100)
    num_of_sit = models.CharField(max_length=100)
    sit_number = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    timings = models.CharField(max_length=100)
    date_of_show = models.CharField(max_length=100)
    movie_type = models.CharField(max_length=100)
    date_booked = models.CharField(max_length=100)
    paid_through = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name


class Review(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


