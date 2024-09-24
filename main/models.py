import uuid  # tambahkan baris ini di paling atas
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) #menyimpan nama produk
    price = models.IntegerField() #menyimpan harga produk 
    description = models.TextField() #menyimpan deskripsi produk
    quantity = models.IntegerField(default=0) #menyimpan kuantitas produk

    def __str__(self): #memberikan representasi string dari objek ketika diakses
        return self.name 