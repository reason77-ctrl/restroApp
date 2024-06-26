from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.base import View
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ContactForm, CateringForm, EventManagementForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.

class HomeView(View):

    def get(self,request):
        slider = Slider.objects.all()
        img_slides = ImageSlider.objects.filter(status = 'active')
        categories = Category.objects.all()
        abouts = About.objects.all()
        reviews = Review.objects.filter(status = 'active')
        items = Item.objects.all()
        item_already_in_cart = []
        total_cart_item = 0
        # if request.session.has_key('username'):
        username = request.user.username
        cart_items = Cart.objects.filter(username=username).values_list('items', flat=True)
        item_already_in_cart = [item.id for item in items if item.id in cart_items]
        total_cart_item = len(Cart.objects.filter(username=username))
            
        
        context = {
            'slider':slider,
            'img_slides':img_slides,
            'categories':categories,
            'items':items,
            'abouts':abouts,
            'reviews':reviews,
            'nbar': 'home',
            'item_already_in_cart':item_already_in_cart,
            'total_cart_item':total_cart_item,
        }
        
        return render(request,'index.html',context)



class MenuView(View):

    def get(self,request):
        # items = Item.objects.all()
        categories = Category.objects.all()

        paginator = Paginator(Item.objects.all(), 1)
        page = request.GET.get('page')
        items = paginator.get_page(page)
        total_pages = items.paginator.num_pages

        item_already_in_cart = []
        total_cart_item = 0
        username = request.user.username
        cart_items = Cart.objects.filter(username=username).values_list('items', flat=True)
        item_already_in_cart = [item.id for item in items if item.id in cart_items]
        total_cart_item = len(Cart.objects.filter(username=username))

        context = {
            'items':items,
            'categories':categories,
            'totalPageList':[n+1 for n in range(total_pages)],
            'nbar':'menus',
            'item_already_in_cart':item_already_in_cart,
            'total_cart_item':total_cart_item,
        }
        return render(request, 'menu.html', context)



class GalleryView(View):
    
    def get(self,request):
        username = request.user.username
        total_cart_item = 0
        total_cart_item = len(Cart.objects.filter(username=username))
        gallery = Gallery.objects.all()

        context = {
            'nbar':'gallery',
            'total_cart_item':total_cart_item,
            'gallery':gallery,
        }
        return render(request, 'gallery.html', context)


class PlacesNearbyView(View):

    def get(self,request):
        username = request.user.username
        total_cart_item = 0
        total_cart_item = len(Cart.objects.filter(username=username))
        placesNearby = PlacesNearby.objects.all()
        context = {
            'nbar':'placesNearby',
            'total_cart_item':total_cart_item,
            'placesNearby':placesNearby,
        }
        return render(request, 'placesNearby.html', context)



class CateringView(View):

    def get(self,request):
        form = CateringForm()
        username = request.user.username
        total_cart_item = 0
        total_cart_item = len(Cart.objects.filter(username=username))
        context = {
            'nbar':'catering',
            'form':form,
            'total_cart_item':total_cart_item,
        }

        return render(request, 'catering.html', context)
    
    def post(self,request):
        form = CateringForm()
        if request.method == 'POST':
            form = CateringForm(request.POST)
            if form.is_valid():
                full_name = form.cleaned_data["full_name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]

                send_mail(
                    subject='Catering Order',
                    message=f"Name: {full_name}\nEmail: {email}\nPhone: {phone}",
                    from_email=email,
                    recipient_list=["admin@example.com"],
                    fail_silently=False,
                )
                form.save()
                messages.success(request, 'Message has been sent!!')
                
                return redirect('home:catering')
        return render(request,'catering.html',{'form':form})


class EventMgmtView(View):

    def get(self, request):
        form = EventManagementForm()
        username = request.user.username
        total_cart_item = 0
        total_cart_item = len(Cart.objects.filter(username=username))
        context = {
            'nbar':'eventMgmt',
            'form':form,
            'total_cart_item':total_cart_item,
        }

        return render(request, 'eventMgmt.html', context)
    
    def post(self,request):
        if request.method == 'POST':
            form = EventManagementForm(request.POST)
            if form.is_valid():
                full_name = form.cleaned_data["full_name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]

                send_mail(
                    subject='Event Management Order',
                    message=f"Name: {full_name}\nEmail: {email}\nPhone: {phone}",
                    from_email=email,
                    recipient_list=["admin@example.com"],
                    fail_silently=False,
                )
                
                messages.success(request, 'Message has been sent!!')
                form.save()
                return redirect('home:event-manage')
        return render(request,'eventMgmt.html')



class ContactUsView(View):

    def get(self,request):
        form = ContactForm()
        username = request.user.username
        total_cart_item = 0
        total_cart_item = len(Cart.objects.filter(username=username))
        context = {
            'nbar': 'contact-us',
            'form':form,
            'total_cart_item':total_cart_item,
        }
        return render(request, 'contact.html', context)
    
    def post(self,request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                message = form.cleaned_data["message"]

                send_mail(
                    subject='Contact Form Submission',
                    message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
                    from_email=email,
                    recipient_list=["admin@example.com"],
                    fail_silently=False,
                )
                messages.success(request, 'Message has been sent!!')
                form.save()
                return redirect('home:contact-us')
        return render(request,'contact.html')
    


class CartView(View):

    def get(self,request):
        username = request.user.username
        total_cart_item = 0
        total_cart_item = len(Cart.objects.filter(username=username))
        carts = Cart.objects.filter(username=username)
        cart_id = Cart.objects.filter(username=username).values_list('id', flat=True)
        total=[]
        for each in cart_id:
            prices = Cart.objects.get(id=each).price
            total.append(prices)
        all_total=sum(total)

                   
        context = {
                'total_cart_item':total_cart_item,
                'carts':carts,
                'all_total':all_total,
            }
        return render(request, 'cart.html', context)


def add_to_cart(request):
        username = request.user.username
        food_id = request.POST.get('food_id')
        food_name = Item.objects.get(id=food_id)
        foods = Item.objects.filter(id = food_id)
        for i in foods:
            cart_image = i.item_image
            price = i.price
            Cart(username=username,items=food_name,cart_image=cart_image,price=price).save()
            return redirect('home:index')


def cart_item_quantity(request):
    # username = request.session['username']
    username = request.user.username
    cart_ids = request.POST.get('cart_id')
    quantity = Cart.objects.get(id=cart_ids).quantity
    food_id = request.POST.get('food_id')
    initial_price = Item.objects.get(id=food_id).price
    total_price = initial_price

    if 'increment' in request.POST:
        quantity += 1
        total_price = total_price*quantity

    elif 'decrement' in request.POST:
        if quantity and total_price >0:
            quantity -= 1
            total_price = total_price*quantity

    Cart.objects.filter(username=username, id=cart_ids).update(quantity=quantity,price=total_price)
    return redirect('home:cart')


def delete_cart(request):
    username = request.user.username
    cart_ids = request.POST.get('cart_id')

    if Cart.objects.filter(id=cart_ids).exists():
        Cart.objects.filter(username=username, id=cart_ids).delete()
    return redirect('home:cart')



def checkout(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            username = request.session['username']
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')

            cart_item = Cart.objects.filter(username=username)
            for each in cart_item:
                qty = each.quantity
                price = each.price
                item_name = each.items
                image = each.cart_image

                OrderDetail(username=username, item_name=item_name, image=image, price=price, qty=qty).save()
            cart_item.delete()
            messages.success(request, 'Your order has been sent!!')

            return redirect('home:cart')
        else:
            return redirect('home:signup')   


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request,user)
            request.session['username'] = username
            return redirect('home:index')
        else:
            return messages.error(request,'Username and Password is incorrect')
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect('home:index')


class SignUpView(View):
    def get(self,request):
        username = request.user.username
        form = SignUpForm()
        total_cart_item = 0
        total_cart_item = len(Cart.objects.filter(username=username))

        context = {
            'form':form,
            'total_cart_item':total_cart_item
        }
        return render(request,'signup.html', context)

    def post(self,request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                email = request.POST.get('email')
                
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email already exist!!')
                    return redirect('home:signup')
            
                else:
                    form.save()
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password1']
                    # first_name = form.cleaned_data['first_name']
                    # last_name = form.cleaned_data['last_name']
                    # email = form.cleaned_data['email']

                    user = authenticate(username=username,password=password)
                    login(request, user)
                    return redirect('home:index')
        return render(request, "signup.html")



def feedback(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        rate = request.POST['rate']
        data = Review.objects.create(
            full_name = full_name,
            phone = phone,
            email = email,
            message = message,
            rate = rate,
        )
        data.save
        return redirect('home:index')
    return render(request, 'index.html')



def book_table_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']

        data = TableBookForm.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            address = address,
            city = city,
            state = state,
            zip_code = zip_code,
        )
        data.save()
        send_mail(
            subject='Table Book Form',
            message=f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\nCity: {city}\nState: {state}\nZip Code: {zip_code}",
            from_email=email,
            recipient_list=["admin@example.com"],
            fail_silently=False,
        )
        return redirect('home:index')
    return render(request, 'index.html')
