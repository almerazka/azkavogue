from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

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

    product_entries = Product.objects.all()

    for items in product_entries:
        products.append({
            'name': items.name,
            'price': items.price,
            'description': items.description,
            'quantity': items.quantity,
        })

    context = {
        'name': 'Muhammad Almerazka Yocendra',
        'class': 'Ilmu Komputer, PBP-C',
        'npm': '2306241745',
        'store_name': 'Azka Vogue',
        'slogan': 'Elevate Your Style, Embrace Elegance',
        'products': products,
    }

# Fungsi ini menggabungkan context dengan template HTML (main.html) dan mengirimkannya sebagai respon kepada pengguna.
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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
