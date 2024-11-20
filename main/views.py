import datetime
import json
from django.urls import reverse
from django.shortcuts import render, redirect, reverse   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
# Ini adalah fungsi yang akan dipanggil setiap kali pengguna mengakses halaman tertentu (misalnya /main/)
def show_main(request):

    context = { 
        'my_name': 'Muhammad Almerazka Yocendra',  # Nama kamu
        'class': 'Ilmu Komputer - PBP C',  # Kelas kamu
        'npm': '2306241745',  # NPM kamu
        'store_name': 'Azka Vogue',  # Nama toko
        'slogan': 'Elevate Your Style, Embrace Elegance',  # Slogan toko
        'username': request.user.username,  # Username dari user yang login
        'last_login': request.user.last_login,  # Last login yang disimpan di cookies
        'messages': messages.get_messages(request),  # Get messages
    }

# Fungsi ini menggabungkan context dengan template HTML (main.html) dan mengirimkannya sebagai respon kepada pengguna.
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, 'Product added successfully!')  # Success message
        return redirect('main:show_main')  # Redirect to show_main
    
    context = {'form': form}
    return render(request, 'create_product_entry.html', context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def validate_password(password):
    # Cek panjang minimum
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    
    # Cek apakah ada huruf besar
    if any(char.isupper() for char in password):
        raise ValidationError("Password shouldn't contain uppercase letter.")
    
    # Cek apakah ada huruf kecil
    if not any(char.islower() for char in password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    
    # Cek apakah ada angka
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one digit.")
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            # Validasi tambahan untuk memastikan kedua password sama
            if password1 != password2:
                form.add_error('password2', ValidationError("Passwords do not match."))
            else:
                try:
                    # Validasi syarat password
                    validate_password(password1)
                    # Simpan pengguna baru
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
                except ValidationError as e:
                    form.add_error('password1', e)
        else:
            # Jika form tidak valid, mungkin Anda ingin menampilkan pesan kesalahan
            messages.error(request, "Registration failed. Please check your details.")
    
    else:
        form = UserCreationForm()
        
    context = {'form': form}
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
            for error in form.non_field_errors():
                messages.error(request, error)  # Menyimpan pesan error
            for field in form:
                for error in field.errors:
                    messages.error(request, error)  # Menyimpan pesan error spesifik

    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)
               
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) 
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    user = request.user

    # Validasi: Periksa apakah name atau description mengandung tag HTML
    if '<' in request.POST.get("name") or '>' in request.POST.get("name") or \
       '<' in request.POST.get("description") or '>' in request.POST.get("description"):
        messages.error(request, "This field cannot be blank")
        return HttpResponse("This field cannot be blank", status=400)

    # Buat produk baru
    new_product = Product(
        name=name,
        description=description,
        price=price,
        quantity=quantity,
        user=user
    )

    new_product.save()
    messages.success(request, 'Product added successfully!') 
    return redirect('main:show_main')

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,
            product=data["product"],
            price=int(data["price"]),
            description=data["description"],
            quantity=int(data["quantity"]),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)