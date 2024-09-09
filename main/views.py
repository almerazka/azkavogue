from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Isi Something ',
        'price': '1.000.000',
        'description': 'Gatau cok bingung ngisi apa'
    }

    return render(request, "main.html", context)
