from django.contrib import admin
from .models import *

# Register your models here.

class ImgSliderAdmin(admin.ModelAdmin):
    list_display = ['title','status','date_field']

admin.site.register(ImageSlider,ImgSliderAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','date_field']

admin.site.register(Slider,SliderAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name', 'date_field']
    list_display_links = ['id','cat_name']

admin.site.register(Category,CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','item_name', 'date_field']
    list_display_links = ['id','item_name']

admin.site.register(Item, ItemAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','date_field']

admin.site.register(About, AboutAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','date_field']

admin.site.register(Review, ReviewAdmin)


class BookingFormAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','date_field']

admin.site.register(BookingForm, BookingFormAdmin)


class TableBookFormAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','date_field']

admin.site.register(TableBookForm, TableBookFormAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','phone','date_field']

admin.site.register(ContactUs, ContactUsAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','items','date_field']

admin.site.register(Cart, CartAdmin)