import uuid  # Tambahkan baris ini di paling atas
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Menambahkan UUID sebagai primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Menghubungkan produk dengan pengguna
    name = models.CharField(max_length=255)  # Menyimpan nama produk
    price = models.IntegerField()  # Menyimpan harga produk 
    description = models.TextField()  # Menyimpan deskripsi produk
    quantity = models.IntegerField(default=0)  # Menyimpan kuantitas produk
    image = models.ImageField(upload_to='products/', blank=True, null=True) # Menyimpan gambar produk

    def __str__(self):  # Memberikan representasi string dari objek ketika diakses
        return self.name