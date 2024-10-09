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
- [Tugas 5 PBP 2024/2025](https://github.com/almerazka/azkavogue/wiki/Tugas-5-PBP-2024-2025)

---
# Tugas 6 PBP 2024/2025
### 🫐 1. Jelaskan manfaat dari penggunaan `JavaScript` dalam pengembangan aplikasi web!
Penggunaan `JavaScript` dalam pengembangan aplikasi web memberikan banyak manfaat, di antaranya :

  **1. Sistem Interaksi yang Lebih Dinamis** :  
  
  - `JavaScript` mendukung `WebSocket` dan `AJAX` untuk melakukan komunikasi _real-time_ antara `server` dan `klien`. `JavaScript` sendiri memungkinkan _developer_ membuat aplikasi web yang interaktif. Misalnya, ketika kita mengubah elemen halaman seperti _konten_, _form_, atau _tombol_, perubahan tersebut dapat terjadi secara langsung tanpa harus _merefresh_ seluruh halaman. Hal ini akan menciptakan pengalaman pengguna yang lebih responsif dan menarik. 
    
 **2. Proses Pengolahan Data di Sisi Klien** :  
  
  - `JavaScript` dapat memproses data langsung di browser pengguna _(client-side)_, meningkatkan kecepatan aplikasi, dan mengurangi beban server. Jadi validasi input dapat dilakukan di _(client-side)_ sebelum dikirimkan ke server sehingga mengurangi jumlah kesalahan yang sampai ke _backend_.

  **3. Sisi `Frontend` dan `Backend`** :  
  
  - Dengan `JavaScript`, kita bisa menggunakan bahasa yang sama di _frontend_ dan _backend_. Jadi, kalau kita membuat aplikasi, kita cuma perlu memahami satu bahasa saja untuk semuanya, sehingga pekerjaan akan lebih mudah dan lebih cepat, karena kita tidak perlu memahami dua bahasa yang berbeda untuk bagian _frontend_ dan _backend_ nya.

  **4. Kompatibilitas dan Ekstensibilitas** :  
  
  - `JavaScript` didukung oleh semua browser modern dan dapat berjalan di berbagai _platform_ tanpa perlu instalasi tambahan. Selain itu, ekosistem `JavaScript` sangat luas dengan banyak pustaka dan _framework_ seperti `React`, `Vue`, atau `Angular` yang memudahkan pengembangan fitur kompleks.
  
 ---
### 🥣 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()` ! Apa yang akan terjadi jika kita tidak menggunakan `await`?

Fungsi dari penggunaan `await` saat menggunakan `fetch()` dalam `JavaScript` adalah untuk menunggu sampai proses `fetch()` selesai mengambil data dari server sebelum melanjutkan eksekusi kode berikutnya. Dengan kata lain, `await` memastikan bahwa program tidak akan melanjutkan baris berikutnya hingga `fetch()` selesai mengembalikan _respons_. Ini penting karena `fetch()` adalah fungsi asinkron yang bekerja secara _promise-based_, artinya prosesnya bisa berlangsung tanpa menghalangi eksekusi kode lain.

Jika kita tidak menggunakan `await`, pemanggilan `fetch()` akan mengembalikan sebuah _promise_ yang belum diselesaikan, dan kode akan langsung dieksekusi ke baris berikutnya sebelum data diterima. Ini berarti kita tidak akan mendapatkan data dari permintaan karena eksekusi kode tidak menunggu hasilnya.
```python
   async function getProductEntries() {
        return fetch("{% url 'main:show_json' %}")
            .then((res) => res.json());
    }
   async function refreshProductEntries() {
        document.getElementById("product_entry_cards").innerHTML = "";  // Clear existing entries
        document.getElementById("product_entry_cards").className = "";
        const productEntries = await getProductEntries(); // Fetch product entries
        let htmlString = "";
        let classNameString = "";
```

---
### 🥑 3.  Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk `AJAX` POST?       
Decorator `@csrf_exempt` digunakan untuk menonaktifkan mekanisme perlindungan **CSRF (Cross-Site Request Forgery)** di `Django` pada view tertentu, terutama untuk request `AJAX POST`. Django sendiri menggunakan **CSRF protection** untuk memastikan bahwa ketika data dikirim ke server melalui `POST` _(misalnya, mengisi formulir)_, permintaan berasal dari sumber yang valid/sah. Prosesnya, `Django` akan memeriksa token khusus `(CSRF token)` setiap kali ada request `POST` untuk menghindari serangan jahat yang mencoba menggunakan sesi pengguna tanpa sepengetahuan mereka.

Namun, ketika data dikirim melalui `AJAX POST` _(misalnya, ketika mengirim data tanpa memuat ulang halaman)_, `Django` bisa menolak permintaan ini karena `AJAX` tidak selalu menyertakan `token CSRF`. Sehingga kita perlu menggunakan `@csrf_exempt` agar kita dapat memberi tahu `Django` untuk mengabaikan pemeriksaan token tersebut di view ini dan request bisa diterima meski tanpa token.

Penggunaan `@csrf_exempt` juga harus dilakukan secara hati-hati karena kita menonaktifkan perlindungan penting yang mencegah serangan CSRF. Idealnya, kita hanya menggunakan decorator ini pada view tertentu yang _benar-benar_ memerlukan pengecualian dan memastikan bahwa data yang diterima tetap aman.

---
###  🍋 4.  Pembersihan data input pengguna dilakukan di belakang `(backend)` juga. Mengapa hal tersebut tidak dilakukan di `frontend` saja?

Meskipun validasi di `frontend` telah dilakukan dan dapat menangkap kesalahan input yang lebih cepat, pembersihan data input di `backend` juga sangat penting karena alasan keamanan dan keandalan aplikasi. `Frontend` tidak boleh dijadikan satu-satunya garis pertahanan. Secara singkat, `frontend` berperan sebagai lapisan perlindungan pertama, dan `backend` berperan sebagai lapisan pertahanan utama.

**1. Keamanan** :  
  
  - Pengguna dapat memanipulasi kode `frontend`, seperti mematikan validasi `JavaScript` atau mengirimkan request langsung ke server tanpa melewati `frontend`. Jika tidak ada validasi atau pembersihan di backend, aplikasi bisa rentan terhadap serangan seperti   `injeksi SQL`, `XSS (Cross-Site Scripting)`, atau `code injection`.
    
**2. Keandalan dan Konsistensi Data** :  
  
  - `Frontend` dapat bervariasi di berbagai platform, seperti pada perangkat yang berbeda atau browser yang berbeda. Dengan validasi di `backend`, kita dapat memastikan bahwa semua input sesuai dengan format yang benar sebelum diproses lebih lanjut, kita juga dapat memastikan bahwa data yang masuk konsisten dan sesuai standar aplikasi terlepas dari bagaimana data tersebut dikirim.
    
**Contoh :**
Misalnya, pada sebuah toko online, di `frontend` kita melakukan validasi bahwa pengguna hanya bisa memesan maksimal 5 unit barang sekaligus. Namun, tanpa validasi `backend`, pengguna bisa melakukan _bypass_ pada aturan `frontend` dan mengirimkan permintaan (request) langsung ke server untuk memesan 100 unit barang. Jika tidak ada validasi di `backend`, permintaan tersebut bisa diproses oleh server dan stok barang mungkin akan berkurang dengan cara yang tidak sesuai aturan toko.

---
### 🔰 Langkah Pengimplementasian AJAX
1. **Buatlah fungsi view baru untuk menambahkan produk baru ke dalam basis data dalam bentuk AJAX**
   
     Untuk mengubah `GET` menjadi `AJAX`, saya menambahkan view tambahan pada `views.py` yaitu
     ```python
      @csrf_exempt
      @require_POST
      def add_product_entry_ajax(request):
          name = strip_tags(request.POST.get("name")) 
          description = strip_tags(request.POST.get("description"))
          price = request.POST.get("price")
          quantity = request.POST.get("quantity")
          user = request.user
      
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
     ```        
     
2. **Buatlah path `/create-ajax/` yang mengarah ke fungsi view yang baru dibuat.**

   View tadi akan dipanggil melalui `fetching javascript`, sehingga kita memerlukan perubahan pada `urls.py`
      ```python
           urlpatterns = [
           ...
           path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
          ]
      ```

3. **Ubahlah kode cards data mood agar dapat mendukung AJAX GET**

   Untuk melakukan langkah ini, saya menghapus `block conditional` yang menampilkan `card_product` ketika kosong atau tidak. Sebagai gantinya, saya menambahkan sebuah `div ber-id product-container`. Div ini nantinya akan dimanipulasi secara DOM melalui `script Javascript`, yaitu dengan menambahkan fungsi _asynchronous_ `getProductEntries()` dan `refreshProductEntries()`. Fungsi ini akan melakukan pengambilan data ke `API` product secara `async`. Jika berhasil, maka tampilan dari view product akan diubah sehingga div akan memuat product-product yang telah di `fetch` sebelumnya.
   ```python
        async function getProductEntries() {
          return fetch("{% url 'main:show_json' %}")
           .then((res) => res.json());
        }
      
        async function refreshProductEntries() {
          document.getElementById("product_entry_cards").innerHTML = "";  // Clear existing entries
          document.getElementById("product_entry_cards").className = "";
          const productEntries = await getProductEntries(); // Fetch product entries
          let htmlString = "";
          let classNameString = "";
          ...

      ```
   
4. **Lakukan pengambilan data mood menggunakan `AJAX GET`. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang `logged-in`.**
   
    - Untuk melakukan hal ini, saya mengubah baris pertama pada fungsi `show_json` dan `show_xml` sehingga menjadi

      `data = ProductEntry.objects.filter(user=request.user)`.
      
    - Fungsi `show_json` nantinya akan dipanggil pada fungsi `asynchronous getProductEntries()` sehingga dapat dipastikan bahwa data yang diambil hanyalah data milik pengguna yang sedang `login`

5. **Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product**
   
     ```python
           <!-- Tombol Add New Product Entry by AJAX -->
           <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-500
           hover:bg-indigo-400 text-white font-bold py-3 px-5 rounded-full transition duration-200 ease-in-out
           transform hover:-translate-y-1 hover:scale-110" onclick="showProductModal();">
                Add New Product Entry by AJAX
           </button>
      ```
    Jika button diklik, maka sebuah `modals` akan terbuka. Untuk itu kita membutuhkan kode untuk membuka dan menutup `modals` yang dipakai
     ```python
           function showProductModal() {
               const productModal = document.getElementById('productModal');
               const productModalContent = document.getElementById('productModalContent');
    
               productModal.classList.remove('hidden'); 
               setTimeout(() => {
                  productModalContent.classList.remove('opacity-0', 'scale-95');
                  productModalContent.classList.add('opacity-100', 'scale-100');
               }, 50); 
           }

           function hideProductModal() {
               const productModal = document.getElementById('productModal');
               const productModalContent = document.getElementById('productModalContent');
    
               productModalContent.classList.remove('opacity-100', 'scale-100');
               productModalContent.classList.add('opacity-0', 'scale-95');
    
               setTimeout(() => {
                     productModal.classList.add('hidden');
               }, 150); 
          }

          document.getElementById("cancelProductButton").addEventListener("click", hideProductModal);
          document.getElementById("closeProductModalBtn").addEventListener("click", hideProductModal);
          document.getElementById("productEntryForm").addEventListener("submit", (e) => {
              e.preventDefault();
              addProductEntry();
          })
      ```
6. **Buatlah fungsi baru pada block `<script>` untuk menambahkan data product dengan `AJAX`**
      ```python
           function addProductEntry() {
             ...
           }
      ```

7. **Hubungkan form yang telah kita buat di dalam modal ke path `/create-ajax/`**

   Form dalam `modals` akan dihubungkan ke path `/create-ajax/` melalui `fetch()` yang ada di dalam fungsi `addProduct()`
     ```python
           function addProductEntry() {
              event.preventDefault();
              document.getElementById("error-message").innerHTML = "";
              fetch("{% url 'main:add_product_entry_ajax' %}", {
                 method: "POST",
                 body: new FormData(document.querySelector('#productEntryForm')),
                 headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                 },
           })
           ...
      ```

8. **Lakukan _refresh_ pada halaman utama secara _asinkronus_ untuk menampilkan daftar product terbaru tanpa _reload_ halaman utama secara keseluruhan.**
    
      Memasukkan fungsi `refreshProducts()` ke fungsi `addProduct()` sehingga setiap kali tombol `submit` ditekan/produk baru ditambahkan, halaman akan `direfresh` secara `asinkronus`.
      ```python
           function addProductEntry() {
              ...
              .then(response => {
                  if (response.ok) {
                      refreshProductEntries();
                      document.getElementById("productEntryForm").reset(); 
                      hideProductModal();
                  }
              ...
      ```
