from django.shortcuts import render

# Ini adalah fungsi yang akan dipanggil setiap kali pengguna mengakses halaman tertentu (misalnya /main/)
def show_main(request):
    products = [
        {
            'name': 'Leather Jacket',
            'price': 250.000,
            'description': 'A classic leather jacket that combines style and comfort.',
            'quantity': 30,
        },
        {
            'name': 'Jeans Jacket',
            'price': 140.000,
            'description': 'A trendy jeans jacket for a casual yet stylish look.',
            'quantity': 50,
        },
        {
            'name': 'Corduroy Pants',
            'price': 80.000,
            'description': 'Comfortable and durable corduroy pants for a sophisticated appearance.',
            'quantity': 40,
        },
        {
            'name': 'Graphic T-Shirt',
            'price': 45.000,
            'description': 'A cool graphic t-shirt to express your unique style.',
            'quantity': 100,
        }
    ]

    context = {
        'name': 'Muhammad Almerazka Yocendra',
        'class': 'Ilmu Komputer',
        'npm': '2306241745',
        'store_name': 'Azka Vogue',
        'slogan': 'Elevate Your Style, Embrace Elegance',
        'products': products,
    }

# Fungsi ini menggabungkan context dengan template HTML (main.html) dan mengirimkannya sebagai respon kepada pengguna.
    return render(request, "main.html", context)