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
- [Tugas 4 PBP 2024/2025](https://github.com/almerazka/azkavogue/wiki/Tugas-4-PBP-2024-2025)

---
# Tugas 5 PBP 2024/2025
### 🌱 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan `CSS selector` terjadi ketika ada beberapa aturan CSS yang mencoba mengatur gaya pada elemen HTML yang sama. Jadi `CSS` akan menggunakan _Selector Specificity_ untuk menentukan selector mana sih yang kira-kira akan dipakai. Berikut adalah urutan prioritas dari paling tinggi ke rendah :
1. **Inline styles** : Gaya ini didefinisikan langsung di dalam elemen HTML dengan atribut style. Contoh : `<p style="color: black;">`
2. **ID selectors** : Selektor yang menggunakan ID `(#id)`. Contoh : ` #text { color: red; }`
3. **Class selectors** : Selektor yang menggunakan kelas `(.class)` atau pseudo-class seperti `:hover`. Contoh : ` .important { color: blue; }`
4. **Element selectors** : Selektor yang menggunakan nama elemen HTML `(div, h1, p)`. Contoh : `p { color: green; }`

Ada satu hal lagi yaitu, `!important`. `!important` memang tidak masuk ke dalam _selector specificity_, `!important` sendiri berada **di luar** aturan spesifisitas dan memiliki **prioritas tertinggi** dalam urutan pengambilan keputusan CSS. Ini bisa dibilang bahwa aturan dengan `!important` akan mengabaikan _spesifisitas selector_ dan selalu diterapkan di atas aturan CSS lainnya, **kecuali** ada aturan lain dengan `!important` yang lebih spesifik atau ditulis terakhir. Jadi yang diambil yang terakhir.
### Contoh :
```html
<p id="heading" class="title">Hello CSS</p>
```
```css
<style>
  p { color: green; }          /* Element selector */
  .title { color: blue; }       /* Class selector */
  #heading { color: red; }      /* ID selector */
</style>
```
Dalam contoh ini _tidak ada_ gaya inline yang ditetapkan pada elemen `<p>`, hasil akhirnya adalah teks akan diwarnai **merah** dari aturan ID selector #heading. **Contoh lain** :
```html
<p id="heading" class="title" style="color: purple;">Hello CSS</p>
```
Berbeda seperti tadi disini terdapat _inline style_, sehingga _inline style_ akan memiliki prioritas tertinggi, dan teks akan diwarnai **ungu**.

---
### 🌺 2. Mengapa _responsive design_ menjadi konsep yang penting dalam pengembangan aplikasi `web`? Berikan **contoh aplikasi** yang sudah dan belum menerapkan _responsive design_!
_Responsive Design_ menjadi konsep penting dalam pengembangan aplikasi web karena berbagai alasan terutama terkait peningkatan `pengalaman pengguna`, `aksesibilitas`, dan `SEO`.

  - **Pengalaman pengguna** :
    _Responsive design_ memastikan tampilan dan fungsi aplikasi yang dibuat dapat menyesuaikan diri di berbagai perangkat, entah dari `smartphone`, `dekstop`, `tablet` ataupun yang lain. Terlebih lagi di era digital saat ini, dimana semua orang mengenggam `smartphone`, hal ini akan membuat pengguna merasa lebih nyaman dan tidak perlu _zoom in_ atau _zoom out_ untuk melihat suatu konten.

   - **Aksesibilitas** :
     Dengan lebih banyak pengguna yang mengakses, _responsive design_ memungkinkan aplikasi `web` diakses dengan baik di berbagai perangkat serta meningkatkan jangkauan _audiens_.

   - **SEO (Search Engine Optimization)** :
     Contohnya adalah Google. Google memberikan preferensi pada situs web yang responsif, sehingga meningkatkan peringkat pencarian. Dengan menggunakan _responsive design_ pemilik situs seperti Google dapat menghindari masalah duplikat konten, karena jadinya dekstop dan mobile tidak dalam versi terpisah serta memastikan pengalaman user yang konsisten

### Contoh :
   - Aplikasi Web yang Sudah Menerapkan Responsive Design
        - `Instagram, Youtube, Google` : Tampilan aplikasi ini sudah secara otomatis disesuaikan dengan perangkat yang digunakan
   - Aplikasi Web yang Belum Menerapkan Responsive Design
        - `SIAK-NG, Si Asisten` : Aplikasi ini memiliki tampilan yang sama walaupun diakses dengan perangkat yang berbeda
---
### 🍄 3.  Jelaskan perbedaan antara `margin`, `border`, dan `padding`, serta cara untuk mengimplementasikan ketiga hal tersebut!                                                                        |
![Screenshot 2024-10-02 091407](https://github.com/user-attachments/assets/1133359c-304b-4333-92fb-6d72cd16a5c0)

   **1. Margin** :  
        **Margin adalah** ruang kosong di luar elemen yang memisahkan elemen tersebut dari elemen lain di sekitarnya. **Margin** tidak memengaruhi ukuran elemen itu sendiri. **Margin** biasanya digunakan untuk mengatur jarak antar elemen, baik di atas, bawah, kanan, atau kiri elemen agar tidak saling berdempetan atau menempel ke tepi container.
```css
  .container {
    margin-top: 10px;     /* Menambahkan jarak 10px di atas elemen */
    margin-bottom: 20px;  /* Menambahkan jarak 20px di bawah elemen */
    margin-left: 15px;    /* Menambahkan jarak 15px di kiri elemen */
    margin-right: 5px;    /* Menambahkan jarak 5px di kanan elemen */
    /* Atau */
    margin: 40px 20px 15px 20px; /* Atas Bawah Kanan Kiri */
  }
  ```
  **2. Border** :  
        **Border adalah** garis yang mengelilingi elemen, tepat di luar _padding_. **Border** membentuk batas visual antara elemen dengan sekitarnya. **Border** sendiri memberikan batas tepi yang jelas di sekitar elemen. Border dapat diatur ketebalannya, warnanya, dan jenis garisnya.
```css
  .container {
    border-width: 5px;     /* Ketebalan border 5px */
    border-style: dashed;  /* Style border: garis putus-putus */
    border-color: blue;    /* Warna border biru */
    /* Atau bisa disingkat */
    border: 5px dashed blue; 
  }
```
  **3. Padding** :  
        **Padding adalah** riang di dalam elemen, antara konten elemen dan border. Padding menambah ruang di dalam elemen, tetapi tetap dalam area elemen tersebut. **Padding** berfungsi untuk menambahkan ruang di dalam elemen agar konten tidak bersentuhan langsung dengan border.
```css
  .container {
    padding: 20px;         /* Menambahkan padding 20px di semua sisi elemen */
    /* Atau bisa spesifik */
    padding-top: 10px;     /* Menambahkan padding 10px di atas elemen */
    padding-bottom: 15px;  /* Menambahkan padding 15px di bawah elemen */
    padding-left: 5px;     /* Menambahkan padding 5px di kiri elemen */
    padding-right: 25px;   /* Menambahkan padding 25px di kanan elemen */
  }
```
| **Komponen** | **Definisi** | **Fungsi** | **Penampilan** |                                                            
|--------------|--------------|------------|----------------|
| **Margin**   | Ruang di luar border yang memisahkan elemen-elemen HTML satu dengan lainnya. | Memberikan jarak antar elemen | Transparan, tidak mempengaruhi konten. |  
| **Border**   | Garis tepi yang mengelilingi elemen, berada di antara margin dan padding | Mengelilingi elemen dengan garis, warna, dan gaya | Dapat diubah warna, ketebalan, dan gaya |
| **Padding**  | Ruang di dalam border yang memberikan jarak antara konten dan border | Memberikan jarak antara konten dan border | Transparan, hanya menggeser konten |

---
### 💐 4. Jelaskan konsep Flexbox dan grid layout beserta kegunaannya!
- **Flexbox (Flexible Box Layout) adalah** metode tata letak yang dirancang untuk mengatur elemen dalam _satu dimensi_, baik secara `horizontal` (baris) maupun `vertikal` (kolom).
- **Kegunaan :**
    - Menyusun elemen dalam satu baris atau satu kolom dengan fleksibel.
    - Mengatur elemen agar responsif terhadap ukuran layar, baik diperbesar maupun diperkecil
    - Membuat tata letak yang dinamis tanpa harus menentukan ukuran tetap.
- **Contoh yang saya gunakan** : Menata harga dan kategori produk secara horizontal
```css
<div class="flex justify-between items-center mb-2">
```
- **Grid Layout adalah** sistem dua dimensi untuk mengatur elemen dalam baris dan kolom. Dengan Grid, kita dapat membuat tata letak yang lebih kompleks dibandingkan `Flexbox`, seperti feeds galeri kita karena Grid memungkinkan penataan elemen dalam dua dimensi secara bersamaan, yaitu `horizontal` dan `vertikal`.
- **Kegunaan :**
    - Membuat tata letak yang lebih rumit seperti halaman dashboard, galeri, atau struktur yang membutuhkan kontrol lebih terhadap baris dan kolom.
    - Memungkinkan untuk mengatur grid yang fleksibel dengan jumlah kolom dan baris yang dapat berubah sesuai dengan ukuran layar.
- **Contoh yang saya gunakan** : Menata harga dan kategori produk secara horizontal
```css
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
```

---
### 🔰 Langkah Pengimplementasian 
1. **Mengimplementasikan Fungsi Menghapus dan Mengedit**
    - Menambahkan fungsi-fungsi berikut pada berkas `views.py` di direktori `main`
         ```python
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
         ```
     
2. **Import Fungsi dan tambahkan path `URL` nya**
    - Import fungsi yang dibuat sebelumnya ke dalam berkas `urls.py` pada `main` dan menambahkan path url nya
      ```python
            from main.views import edit_product
            from main.views import delete_product
    
            urlpatterns = [
              ...
              path('edit-product/<uuid:id>', edit_product, name='edit_product'),
              path('delete/<uuid:id>', delete_product, name='delete_product'),
            ]
      ```

3. **Kustomisasi halaman `login`, `register`, dan `tambah product` dengan menggunakan Tailwind**
    - Menggunakan tailwind untuk memberi style pada `login`, `register`, dan `addproduct`.
      - [Login Page](https://github.com/almerazka/azkavogue/blob/main/main/templates/login.html)
      - [Register Page](https://github.com/almerazka/azkavogue/blob/main/main/templates/register.html)
      - [Add Product](https://github.com/almerazka/azkavogue/blob/main/main/templates/create_product_entry.html)

4. **Membuat dan kustomisasi halaman `card_product`, `card_info`, dan `edit_product` dengan menggunakan CSS Framework (Tailwind)**
    - Menggunakan tailwind untuk memberi style pada `card_product`, `card_info`, dan `edit_product`.
      - [Card Product](https://github.com/almerazka/azkavogue/blob/main/main/templates/card_product.html) : `card_product.html` berisi tampilan dari product product yang ada dan juga memiliki button edit dan hapus product. Terakhir kita panggil card_product itu di `main.html` menggunakan include.
      - [Card Info](https://github.com/almerazka/azkavogue/blob/main/main/templates/card_info.html)
      - [Edit Product](https://github.com/almerazka/azkavogue/blob/main/main/templates/edit_product.html)

5. Membuat folder static/image untuk menyimpan gambar. Kemudian menambahkan image tersebut ke main.html untuk menampilkan gambar jika belum ada data product yang tersimpan
    - Jangan lupa tambahkan {% load static %} untuk menggunakannya
    
6. Menambahkan konfigurasi file static dengan cara menambahkan `whitenoise.middleware.WhiteNoiseMiddleware` ke middleware, lalu menambahkan `STATICFILES_DIRS` dan juga `STATIC_ROOT`.
      ```python
            STATIC_URL = '/static/'
            if DEBUG:
                STATICFILES_DIRS = [
                    BASE_DIR / 'static' # merujuk ke /static root project pada mode development
                ]
            else:
                STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
      ```

7. Membuat responsive navbar pada `base.html` di folder templates luar project menggunakan tailwind dan mengitegrasikannya dengan `mobile-view`
      - [Navigation Bar](https://github.com/almerazka/azkavogue/blob/main/templates/base.html)
