from django.db import models
from django.urls import reverse

# Create your models here.

STATUS = (
    ('active','active'),
    ('inactive','inactive'),
)

RATING = (
    ('1 Star', '1 Star'),
    ('2 Star', '2 Star'),
    ('3 Star', '3 Star'),
    ('4 Star', '4 Star'),
    ('5 Star', '5 Star'),
)


class ImageSlider(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slider_img = models.ImageField(upload_to='media/slider-img',blank=True)
    status = models.CharField(choices=STATUS, max_length=100, blank=True)
    date_field = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name
    

class Item(models.Model):
    item_image = models.ImageField(upload_to='item-img', blank=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
    

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=150, blank=True)
    message = models.TextField()
    rate = models.CharField(max_length=100, choices=RATING)
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class CateringBook(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    date_field = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.full_name



class EventBook(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    date_field = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.full_name



class TableBookForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=50)
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    date_field = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media/gallery', blank=True)
    date_field = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class PlacesNearby(models.Model):
    pass
    # title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='media/gallery')
    # date_field = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    # def __str__(self):
    #     return self.title


class Cart(models.Model):
    username = models.CharField(max_length=100,null=True)
    cart_image = models.ImageField(upload_to='media/cart_img')
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    date_field = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.username
    


class OrderDetail(models.Model):
    username = models.CharField(max_length=100,default=True)
    item_name = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True)
    qty = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
