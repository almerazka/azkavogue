![Screenshot 2024-09-18 101825](https://github.com/user-attachments/assets/3b969c8e-eba4-445f-ae0c-55ba9d497b46)![Screenshot 2024-09-18 101740](https://github.com/user-attachments/assets/e3e856cd-cd7f-48fc-b8b0-bb01c3c9e08a)# AzkaVogue 🎹
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

---
# Tugas 3 PBP 2024/2025
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

**Data delivery** sangat diperlukan dalam pengimplementasian sebuah platform karena _data delivery_ memastikan data dapat dikirim, diterima, dan diproses secara aman, efektif dan efisien di antara berbagai komponen platform, baik antar server, client maupun antar aplikasi dan platform. Tanpa _sistem data delivery_ yang baik, platform tidak dapat berfungsi secara maksimal, bahkan data dapat rusak dan hilang. Proses _data delivery_ ini mencakup pengiriman data secara _real-time_, pengelolaan bandwidth, serta memastikan keamanan data. Hal ini bertujuan agar pengguna tetap mendapatkan akses yang stabil dan dapat dengan mudah memperoleh informasi serta fitur yang mereka butuhkan.

---
### 🧀 Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih banyak digunakan oleh banyak orang daripada XML dalam pengembangan aplikasi modern karena beberapa alasan utama:

   * **Lebih ringkas**
     * JSON memiliki format yang jauh lebih sederhana dan tidak memerlukan tag penutup seperti XML, sehingga mengurangi ukuran data yang dikirim dan disimpan. Ini membuatnya lebih efisien dalam transmisi data.
   * **Mudah dipahami dan ditulis**
     * JSON memiliki sintaks yang lebih sederhana dan mudah dibaca, baik oleh manusia maupun oleh komputer, sehingga mempermudah proses pengembangan dan debugging.
  * **Integrasi alami dengan JavaScript** 
    * JSON bekerja secara langsung dengan `JavaScript`, yang menjadikannya pilihan yang lebih praktis untuk pengembangan aplikasi berbasis web. JSON dapat dengan cepat diparsing melalui metode bawaan seperti `JSON.parse()`, sedangkan XML membutuhkan manipulasi lebih kompleks melalui DOM.
  * **Efisiensi dalam aplikasi web modern**
    * Dalam konteks AJAX dan API berbasis web, JSON memberikan kinerja yang lebih baik, memungkinkan pertukaran data yang lebih cepat dan lebih mudah dikelola.

Meskipun XML memiliki keunggulan seperti skema validasi dan penggunaan namespace, JSON lebih populer karena formatnya yang ringan, cepat, dan sangat kompatibel dengan teknologi web saat ini.

---
### 🍟 Jelaskan fungsi dari `method is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut

Method `is_valid()` pada _form_ di Django berfungsi untuk memvalidasi data yang dimasukkan oleh pengguna ke dalam form. Method ini akan mengecek apakah data yang dikirimkan memenuhi aturan-aturan yang telah ditentukan pada form, seperti tipe data yang benar, panjang maksimum dan minimum, serta validasi khusus lainnya. Berikut penjelasan mengapa kita membutuhkan `method is_valid()`:

  1. **Validasi Data**: Memastikan data sesuai dengan aturan yang ditentukan
  2. **Akses Data yang Dibersihkan**: Ketika `is_valid()` mengembalikan `True`, Django akan menyimpan data yang telah "dibersihkan" (data yang telah lulus validasi) dalam atribut `cleaned_data`.
  3. **Mencegah Penyimpanan Data yang Tidak Valid**: Dengan menggunakan `is_valid()`, kita dapat mencegah proses penyimpanan data yang salah atau tidak valid ke dalam database. 
  4. **Menyediakan Feedback Error**: Ketika `is_valid()` mengembalikan `False`, Django otomatis menyediakan pesan error yang menjelaskan kesalahan spesifik, sehingga memudahkan pengguna untuk memperbaiki input mereka.

---
### 🥞 Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan _Cross-Site Request Forgery (CSRF)_. CSRF adalah jenis serangan di mana penyerang dapat mengirimkan permintaan berbahaya melalui pengguna yang sudah terotentikasi, tanpa sepengetahuan mereka.

Jika kita tidak menambahkan `csrf_token` pada form di Django, hal-hal berikut bisa terjadi:

  1. **CSRF Attack**: 
     * Penyerang bisa membuat skrip yang mengirimkan permintaan berbahaya menggunakan identitas pengguna yang sedang login di situs kita, seperti mengubah data pengguna atau melakukan transaksi tanpa izin.
  2. **Akses Tidak Sah**: 
     * Permintaan palsu ini akan terlihat sah karena berasal dari browser pengguna yang memiliki sesi _login_, sehingga tindakan berbahaya bisa dijalankan.

Penyerang memanfaatkan kurangnya validasi bahwa permintaan yang dikirim benar-benar berasal dari pengguna yang berniat melakukannya. Dengan `csrf_token`, setiap permintaan _form_ diverifikasi sebagai permintaan yang sah, mencegah serangan semacam ini.

---
### 🔰 Langkah Pengimplementasian 
1. **Membuat input form untuk menambahkan objek model pada app sebelumnya**.
   * Membuat _forms.py_ dengan model Product yang bertujuan untuk menerima data Product baru
   ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "quantity"]
    ```
   * Menambahkan fungsi create_product_entry pada _views.py_ yang mengarahkan pengguna dari halaman utama ke halaman input kemudian memvalidasi, memproses, dan menyimpan input.
   ```python
   def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'create_product_entry.html', context)
   ```
   * Menambahkan product_entries = Product.objects.all() pada fungsi _show_main_ (views.py) agar input yang berhasil diterima ditampilkan ketika pengguna mengakses kembali halaman utama (langsung otomatis berubah)
   ```python
    product_entries = Product.objects.all()

    for items in product_entries:
        products.append({
            'name': items.name,
            'price': items.price,
            'description': items.description,
            'quantity': items.quantity,
        })
   ```
   * Membuat HTML baru bernama create_product_entry.html untuk menampilkan form input URL Routing form input dengan menambahkan path URL ke dalam urlpatterns _urls.py_
    ```python
    from django.urls import path
    from main.views import show_main, create_product_entry

    app_name = 'main'
    
    urlpatterns = [
      path('', show_main, name='show_main'),
      path('create-product-entry', create_product_entry, name='create_product_entry'),
    ]
    ```
  
3. **Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID**.
   * Mengimport `HttpResponse` dan `serializers` di _views.py_ dan membuat method _show_xml, show_json, show_xml_by_id_, dan _show_json_by_id_. Untuk show by id perlu menggunakan objects.filter(pk=id) agar dapat mengembalikan object sesuai dengan id yang diinginkan.
    * View untuk JSON dan XML
     ```python
    def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```
    * View untuk JSON by ID dan XML by ID
    ```python
    def show_xml_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ]
    ```
    
4. **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
   Menambahkan rute URL pada _urls.py_. Untuk method show by id perlu tambahan /<str:id>/ pada path urlpatterns.
    ```python
    from django.urls import path
    from main.views import show_main, create_product_entry

    app_name = 'main'
    
    urlpatterns = [
      ................
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```
### 🍿 Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![XML](https://github.com/user-attachments/assets/15ff80df-512f-455e-a447-1edcd5f0a67d)
![JSON](https://github.com/user-attachments/assets/b39b2925-2c05-4794-ac8a-0abf05f237e7)
![XML by ID](https://github.com/user-attachments/assets/b6ee0557-6f72-4b1b-a4f1-439676f100ad)
![JSON by ID](https://github.com/user-attachments/assets/c453432d-8cc2-4a9a-ba9b-40462db71f7c)
