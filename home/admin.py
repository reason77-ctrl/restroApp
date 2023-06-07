from django.contrib import admin
from .models import *

# Register your models here.

class ImgSliderAdmin(admin.ModelAdmin):
    list_display = ['title','status','date_field']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','date_field']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name', 'date_field']
    list_display_links = ['id','cat_name']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','item_name', 'date_field']
    list_display_links = ['id','item_name']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','date_field']



class ReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','date_field']



class CateringBookAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','date_field']



class EventBookAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','phone','date_field']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title','image','date_field']



class TableBookFormAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','date_field']



class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','phone','date_field']



class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','items','date_field']



class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id','username','image','qty','price','ordered_date']


class PlacesNearbyAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id','username','image','qty','price','ordered_date']


admin.site.register(ImageSlider,ImgSliderAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(CateringBook, CateringBookAdmin)
admin.site.register(EventBook, EventBookAdmin)
admin.site.register(TableBookForm, TableBookFormAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(PlacesNearby, PlacesNearbyAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(OrderDetail,CheckoutAdmin)