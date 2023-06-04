from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.base import View
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ContactForm, CateringForm, EventManagementForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.

class HomeView(View):

    def get(self,request):
        slider = Slider.objects.all()
        img_slides = ImageSlider.objects.filter(status = 'active')
        categories = Category.objects.all()
        abouts = About.objects.all()
        reviews = Review.objects.all()
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

        context = {
            'nbar':'gallery',
            'total_cart_item':total_cart_item,
        }
        return render(request, 'gallery.html', context)


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
        form = ContactForm()
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Message has been sent!!')
                form.cleaned_data
                return redirect('home:contact-us')
        return render(request,'contact.html',{'form':form})
    

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
    cart_ids = request.GET.get('cart_id')

    if Cart.objects.filter(id=cart_ids).exists():
        Cart.objects.filter(username=username, id=cart_ids).delete()
    return redirect('home:cart')


class CheckoutView(View):

    def get(self,request):
        return render(request, 'checkout.html')


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


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']

            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('home:index')
    return render(request, "signup.html",{'form':form})



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
        zip = request.POST['zip']

        data = TableBookForm.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone = phone,
            address = address,
            city = city,
            state = state,
            zip = zip,
        )
        data.save()
        return redirect('home:index')
    return render(request, 'index.html')
