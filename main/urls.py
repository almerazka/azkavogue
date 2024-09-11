from django.urls import path
from main.views import show_main

app_name = 'main'

# Menghubungkan root URL ('') dengan fungsi show_main di views.py
urlpatterns = [
    path('', show_main, name='show_main'),
]