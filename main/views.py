import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
# Ini adalah fungsi yang akan dipanggil setiap kali pengguna mengakses halaman tertentu (misalnya /main/)
def show_main(request):
    products = [
        {
            'name': 'Leather Jacket',
            'price': 250000,
            'description': 'A classic leather jacket that combines style and comfort.',
            'quantity': 30,
        },
        {
            'name': 'Jeans Jacket',
            'price': 140000,
            'description': 'A trendy jeans jacket for a casual yet stylish look.',
            'quantity': 50,
        },
        {
            'name': 'Corduroy Pants',
            'price': 80000,
            'description': 'Comfortable and durable corduroy pants for a sophisticated appearance.',
            'quantity': 40,
        },
        {
            'name': 'Graphic T-Shirt',
            'price': 45000,
            'description': 'A cool graphic t-shirt to express your unique style.',
            'quantity': 100,
        }
    ]

    product_entries = Product.objects.filter(user=request.user)

    for items in product_entries:
        products.append({
            'name': items.name,
            'price': items.price,
            'description': items.description,
            'quantity': items.quantity,
        })

    context = { 
        'my_name': 'Muhammad Almerazka Yocendra',  # Nama kamu
        'class': 'Ilmu Komputer - PBP-C',  # Kelas kamu
        'npm': '2306241745',  # NPM kamu
        'store_name': 'Azka Vogue',  # Nama toko
        'slogan': 'Elevate Your Style, Embrace Elegance',  # Slogan toko
        'products': products,  # Produk yang akan ditampilkan
        'username': request.user.username,  # Username dari user yang login
        'last_login': request.COOKIES['last_login'],  # Last login yang disimpan di cookies
    }

# Fungsi ini menggabungkan context dengan template HTML (main.html) dan mengirimkannya sebagai respon kepada pengguna.
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'create_product_entry.html', context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response