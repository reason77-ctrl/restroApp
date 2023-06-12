from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('menus/', MenuView.as_view(), name = 'menus'),
    path('gallery/', GalleryView.as_view(), name = 'gallery'),
    path('catering/', CateringView.as_view(), name = 'catering'),
    path('event-manage/', EventMgmtView.as_view(), name = 'event-manage'),
    path('contact-us/', ContactUsView.as_view(), name = 'contact-us'),
    path('cart/', CartView.as_view(), name = 'cart'),
    path('places_nearby/', PlacesNearbyView.as_view(), name = 'places_nearby'),

    path('cart_item_quantity/', cart_item_quantity, name = 'cart_item_quantity'),
    path('delete_cart/', delete_cart, name = 'delete_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name = 'checkout'),
    
    path('login-user/', login_user, name='login-user'),
    path('logout-user/', logout_user, name='logout-user'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('feedbacks/', feedback, name='feedbacks'),
    path('book-table/', book_table_form, name='book-table'),
]