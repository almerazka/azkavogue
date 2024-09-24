# AzkaVogue 🎹
_AzkaVogue_ adalah aplikasi web berbasis Django untuk menampilkan produk fashion seperti jaket kulit, jaket jeans, dan celana corduroy. Aplikasi ini menunjukkan produk dengan atribut seperti nama, harga, deskripsi, dan kuantitas.

---

### 🧑🏻 Author
- Name   : Muhammad Almerazka Yocendra
- NPM    : 2306241745
- Kelas  : PBP C

### ✨ Deployment
[AzkaVogue Webpage](http://muhammad-almerazka-azkavogue.pbp.cs.ui.ac.id/)

### 🔖 Archive Question
- [Tugas 2 PBP 2024/2025](https://github.com/almerazka/azkavogue/wiki/Tugas-2-PBP-2024-2025)
- [Tugas 3 PBP 2024/2025](https://github.com/almerazka/azkavogue/wiki/Tugas-3-PBP-2024-2025)

---
# Tugas 4 PBP 2024/2025
### 🦜 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
- **`HttpResponseRedirect()`**:
  - `HttpResponse` adalah sebuah objek yang secara eksplisit memberikan instruksi untuk melakukan pengalihan manual dan langsung ke URL tertentu tanpa menggunakan mekanisme atau penanganan tambahan dari Django.
  - `HttpResponseRedirect()` biasanya digunakan ketika kita sudah mengetahui pasti URL yang ingin dituju. Misalnya, jika ada kondisi tertentu dimana kita memerlukan pengalihan ke halaman tertentu, kita bisa menyertakan URL tersebut dalam `HttpResponseRedirect`. Jadi intinya URL nya langsung disertakan dalam kode.
  -  **Contoh** :
   ```python
   def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   ...
   ```
- **`redirect()`**:
  - `redirect` adalah helper function bawaan Django yang secara otomatis membuat objek `HttpResponseRedirect` di balik layar. 
  - `redirect` dapat menerima URL (baik lengkap maupun relatif), view name (nama dari URL yang sudah terdaftar di urls.py), atau objek model.
  - Jika kita tidak tahu pasti URL yang ingin dituju, kita bisa menggunakan `redirect()` dengan nama view atau URL pattern dari `urls.py`. Nanti django akan secara otomatis ngatasin pemetaan dari nama view tersebut jadi URL yang benar. Ini bisa banget kita gunain kalau URL kita bisa berubah atau bergantung pada faktor-faktor lain.
  -  **Contoh** :
   ```python
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
   ```
- **`Perbandingan Utama`** :
  - `HttpResponseRedirect()` hanya menerima URL lengkap/relatif, sedangkan `redirect()` dapat menerima URL, nama view, atau bahkan objek model.
  - `HttpResponseRedirect` memberikan kontrol penuh untuk pengalihan ke URL yang ditentukan secara _eksplisit_, tanpa adanya penanganan **dinamis** dari Django. Untuk `redirect()` sebaliknya.
  - `redirect()` lebih **fleksibel** karena memungkinkan pemetaan ke view tanpa harus menentukan URL pasti atau relatif secara langsung.

---
### 🐙 2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!
Dalam projek kali ini, penghubungan model `Product` dengan `User` dilakukan menggunakan relasi **ForeignKey**. Contohnya
```python
   class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField() 
    description = models.TextField() 
    quantity = models.IntegerField(default=0)
   ```
- Dengan menggunakan **ForeignKey**, setiap Product yang kita buat akan memiliki ID pengguna yang terkait.
- `on_delete=models.CASCADE` digunakan agar ketika pengguna yang memiliki produk dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus.
- **Cara Kerja**
  - Setiap kali pengguna membuat entri produk, produk tersebut akan secara otomatis terkait dengan satu User yang sedang login.
  - Dengan menggunakan **ForeignKey**, relasi _many-to-one_ akan dibuat antara `Product` dan `User`. Hal ini berarti, satu pengguna dapat memiliki banyak produk, tetapi satu produk hanya dapat dimiliki oleh satu pengguna.

---
### 🦚 3. Apa perbedaan antara `authentication` dan `authorization`, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut!
 - **Authentication** : adalah sebuah proses verifikasi dimana kita dapat mengetahui identitas user yang _login_, seperti _usenamenya_ apa?, _passwordnya_ apa?. Ini adalah langkah pertama yang dapat kita lakukan untuk memastikan _website_ kita dapat diakses oleh User yang memilki akun dan telah melewati proses verifikasi. Django menggunakan fungsi `authenticate()` untuk memverifikasi identitas pengguna, dan `login()` untuk mencatat pengguna sebagai terautentikasi.
    - **Contoh** : Proses login di mana pengguna memasukkan nama pengguna dan kata sandi.
 - **Authorization** : adalah sebuah proses verifikasi dimana user yang berhasil _login_ akan ditentukan berhak mengakses apa, seperti apakah halaman web/resource ini bisa diakses olehnya?.  Ini adalah langkah kedua untuk menghindari akses yang tidak sah. 
    - **Contoh**: Setelah _login_, pengguna dapat mengakses data mereka sendiri tetapi tidak dapat mengakses data pengguna lain atau fitur admin tanpa izin yang sesuai.
```python
  def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      ...
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
   ```
**Implementasi**:
- Django menggunakan **middleware** untuk mengelola autentikasi dan otorisasi. Middleware ini secara otomatis memeriksa apakah pengguna sudah terautentikasi dan menyimpan status ini di objek request.
- Django menyediakan beberapa `decorators` untuk mengelola otorisasi secara sederhana. Misalnya, `@login_required` untuk membatasi akses ke tampilan hanya untuk pengguna yang telah terautentikasi.
- Setelah pengguna terautentikasi, informasi tentang pengguna yang terautentikasi disimpan dalam `request.user`

---
### 🐳 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
  - Saat pengguna _login_ menggunakan fungsi `login()`, Django membuat sesi untuk pengguna tersebut. Django menyimpan informasi sesi di server, dan mengaitkannya dengan **session ID** yang unik. **Session ID** ini disimpan dalam **cookie** di browser pengguna.
  - Sedangkan **Cookies** adalah file kecil yang disimpan di perangkat pengguna oleh browser saat mereka mengunjungi situs web. **Cookies** ini menyimpan data seperti _session ID yang telah dienkripsi_. Setiap kali pengguna mengunjungi situs itu lagi, browser akan mengirimkan **cookie** ini kembali ke server, yang memungkinkan Django untuk mengidentifikasi pengguna yang sudah terautentikasi dan mengingat informasi sesi mereka.
  - **Kegunaan Lain dari Cookies**
     - **Menyimpan Preferensi Pengguna** : Seperti bahasa, tema, atau pengaturan tampilan yang dipilih.
     - **Pelacakan Analitik** : **Cookies** digunakan untuk mengumpulkan data analitik perilaku user di situs, seperti halaman yang sering dikunjungi, hal-hal yang disukai, dan lain sebagainya. Hal ini sangat berkaitan ketika kita sedang berada di sebuah situs _onlineshop_, ketika kita mengakses suatu produk, produk yang berkaitan akan terus muncul di halaman utama, atau misalkan ketika kita membuka _web_, muncul iklan suatu produk yang sering kita cari. Sebenarnya teknik ini sudah banyak digunakan oleh perusahaan besar diluar sana.

   - Tidak semua **cookies** aman digunakan, ada kasus dimana cookies berisi informasi sensitif seperti _password_ namun tidak dienkripsi sehingga **cookies** ini memiliki kemungkinan untuk bisa diakses oleh pihak ketiga. Menurut penjelasan Bu Ara di kelas, sebenarnya **Cookie** tidak bersalah, masalah muncul ketika skrip berbahaya _(malicious scripts)_ mendapatkan akses ke **cookies** tersebut dan mencuri informasi yang ada di dalamnya.

### 🔰 Langkah Pengimplementasian 
### 1. **Mengimplementasikan Fungsi Registrasi, Login, dan Logout**
- **Register**
  1. Buat form di dalam sebuah view untuk registrasi menggunakan `UserCreationForm` dengan method `POST`.
  ```python
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
  ```
   2. Buat template `register.html` untuk menampilkan form registrasi.
   3. Lakukan hal yang sama pada Login dan Logout
    
- **Login**
   1. Buat form login di sebuah view untuk login pengguna yang sudah terdaftar.
      ```python
      def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  response = HttpResponseRedirect(reverse('main:show_main'))
                  response.set_cookie('last_login', datetime.datetime.now())
                  return response
      
         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'auth/login.html', context)
      ```
   2. Buat template `login.html` untuk menampilkan form login

- **Logout**
  1. Buat form logout di sebuah view untuk melakukan logout
     ```python
       def logout_user(request):
          logout(request)
          response = HttpResponseRedirect(reverse('main:login'))
          response.delete_cookie('last_login')
          return response
     ```
   2. Tambahkan hyperlink tag logout di template untuk memudahkan user logout melalui logout button:
   ```html
      <a href="{% url 'main:logout' %}">
            <button>Logout</button>
      </a>
   ```

Langkah terakhir semua view dipanggil melalui `urls.py`:
```python
   urlpatterns = [
      .....
      path('register/', register, name='register'),
      path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
  ]
 ```
### 2. **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya**
Melakukan registrasi akun pada page signup/ dengan 2 akun yang berbeda, kemudian login dan tambahkan tiga dummy data pada page create-product-entry/ untuk kedua akun.
![Screenshot 2024-09-24 210724](https://github.com/user-attachments/assets/3ce16a57-a48e-47b1-abd1-3f88b681ec0f)
![Screenshot 2024-09-24 210735](https://github.com/user-attachments/assets/6266672a-7291-4a42-9e54-90d989dbd51c)
![Screenshot 2024-09-24 210750](https://github.com/user-attachments/assets/397abd2a-1598-4a42-88b6-3560d056f1ca)
![Screenshot 2024-09-24 210804](https://github.com/user-attachments/assets/d55fa7e2-321a-4236-b2a8-055cf7a95af8)

### 3. **Menghubungkan model Product dengan User**
Membuat model `Product` dan tambahkan ForeignKey ke `User`, sehingga setiap produk yang dibuat dapat dikaitkan dengan pengguna.
```python
   import uuid  # tambahkan baris ini di paling atas
   from django.db import models
   from django.contrib.auth.models import User

   class Product(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField() 
      quantity = models.IntegerField(default=0)
 ```
Jangan lupa `makemigrations` dan `migrate` setiap membuat perubahan di `models.py` untuk memastikan bahwa database kita diperbarui dengan benar dan berfungsi dengan baik.

### 4. **Menampilkan detail informasi pengguna yang sedang `Logged In`**
- **Menyimpan Data Last Login dan Username saat Login, serta set cookies saat user login**
  ```python
     def login_user(request):
     ...
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
     ...
  ```
- **Mengirim Data Last Login ke Halaman Utama**
  ```python
     product_entries = Product.objects.filter(user=request.user)
     ...
     context = { 
        ...
        'products': products,  # Produk yang akan ditampilkan
        'username': request.user.username,  # Username dari user yang login
        'last_login': request.COOKIES['last_login'],  # Last login yang disimpan di cookies
    }
  ```
- Di template `main.html` tampilkan waktu login terakhir:
  ```html
     ...
     <h5>Sesi terakhir login: {{ last_login }}</h5>
     ...
  ```
  
### 5. **Menampilkan detail informasi pengguna yang sedang `Logged In`**
    - Memodifikasi README.md dan menjawab pertanyaan yang diberikan 
