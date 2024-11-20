from django.urls import path
from authentication.views import login, register
from authentication.views import logout
from main.views import create_product_flutter

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),

]