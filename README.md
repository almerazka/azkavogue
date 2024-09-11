# AzkaVogue
_AzkaVogue_ adalah aplikasi web berbasis Django untuk menampilkan produk fashion seperti jaket kulit, jaket jeans, dan celana corduroy. Aplikasi ini menunjukkan produk dengan atribut seperti nama, harga, deskripsi, dan kuantitas.

## Tautan Aplikasi

## Implementasi Checklist
1. **Membuat Proyek Django Baru**<br>
Setelah membuat sebuah folder untuk proyek Django baru di lokal saya, saya menjalankan virtual environment dan menginstall beberapa requirements, kemudian saya menjalankan perintah `django-admin startproject [nama_proyek]`. Nantinya Django akan secara otomatis menyediakan sebuah struktur dasar yang berisi manage.py, folder myproject/, dan berkas konfigurasi utama seperti settings.py, urls.py, dll

2. **Membuat Aplikasi dengan nama main**<br>
Dengan perintah `python manage.py startapp main`, saya membuat aplikasi baru di dalam proyek django saya dengan nama `main`. Folder ini akan berisi berkas utama seperti _models.py, views.py, urls.py_, dll. Nama aplikasi di Django tidak harus _main_ melainkan disesuaikan dengan kebutuhan proyek.

3. **Melakukan Routing pada Proyek untuk Menjalankan Aplikasi main**<br>
Agar URL dapat diakses dan terhubung dengan _views_ yang sesuai, kita perlu melakukan routing. Jadi setiap kali pengguna mengunjungi URL tertentu di browser, Django perlu mengetahui bagaimana menangani permintaan tersebut dan apa yang harus ditampilkan. Untuk itu =>
- Buka berkas `myproject/settings.py` dan tambahkan aplikasi main ke dalam _INSTALLED_APPS_. (untuk memberi tahu Django bahwa aplikasi main telah dibuat dan akan digunakan dalam proyek)<br>
- Buat file `main/urls.py` dan tambahkan routing dasar untuk aplikasi `main`. (Routing ini akan menghubungkan URL tertentu dengan fungsi-fungsi view di dalam aplikasi) <br>
- Di `myproject/urls.py`, tambahkan routing untuk aplikasi main (menghubungkannya dengan routing utama proyek, saya mengarahkan semua URL yang dimulai dengan `main/` ke routing aplikasi `main`) <br>

4. **Membuat Model Product dengan Atribut name, price, dan description**<br>
Model Product dibuat di dalam `main/models.py` untuk mendefinisikan struktur data yang akan disimpan di database. Perintah `makemigrations` dan `migrate` diperlukan dalam Django untuk mengaplikasikan perubahan tersebut ke dalam database. 
- `makemigrations` (mendeteksi perubahan, misalkan saya menambahkan quantity, ketika `makemigrations` dijalankan Django akan membuat file migrasi yang mencatat bahwa tabel produk di database harus menambahkan kolom _quantity_)<br>
- `migrate` (menjalankan file migrasi yang dihasilkan oleh makemigrations ke dalam database sebenarnya) <br>

5. **Membuat Fungsi pada views.py untuk Menampilkan Nama Aplikasi serta Nama dan Kelas Kamu**<br>
Di `main/views.py`, saya membuat fungsi `show_main` bertanggung jawab untuk mengumpulkan data yang akan dikirimkan ke template HTML dan kemudian menampilkan template tersebut kepada pengguna, disini saya menampilkan nama aplikasi, nama dan kelas saya

6. **Membuat Routing pada urls.py Aplikasi main untuk Mepetakan Fungsi di views.py**<br>
Seperti yang telah saya jelaskan sebelumnya, misalnya, ketika pengguna mengakses */main/*, fungsi *show_main* akan dieksekusi, dan template _main.html_ dengan konteks yang diberikan akan dikirim sebagai respon.

7. **Melakukan Deployment ke PWS**<br>
Setelah aplikasi selesai dan berfungsi dengan baik di lingkungan lokal, deploy ke platform PWS

8. **Membuat README.md dan Jawaban Pertanyaan**<br>
File _README.md_ ini mencakup tautan menuju aplikasi PWS yang sudah di-deploy dan jawaban dari beberapa pertanyaan.

## Jawaban Pertanyaan
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?
Saya memulainya dengan membuat proyek dan aplikasi di Django, menambahkan model Product, mengatur routing dan views, lalu menambahkan data ke dalam template HTML. Setelah pengembangan selesai di lokal, saya melakukan deployment ke PWS. Penjelasan lebih jelas dapat dilihat pada bagian implementasi checklist<br>

### 2. Bagan Request dan Response

Pertama-tama, Client mengirimkan request ke Browser/Internet, kemudian request tersebut akan diproses oleh `urls.py`, dimana _URL Client_ akan dicocokkan dengan _URL Routing_ untuk menentukan `views.py` yang sesuai. Di dalam `views.py` tersebut, logika dijalankan dan jika data dari database diperlukan, fungsi view akan memanggil model di `models.py`. Setelah data berhasil terkumpul, `views.py` akan menyiapkan template HTML dengan data tersebut, lalu merendernya. Hasilnya `main.html` akan dikirimkan ke pengguna untuk ditampilkan. Hasil ini berupa halaman _web_ atau respon JSON yang dikirim kembali ke Browser client.5

### 3. Fungsi Git dalam Pengembangan Perangkat Lunak
1. **Version Control**<br>
Git menyimpan riwayat semua perubahan yang dilakukan pada kode, sehingga memungkinkan programmer untuk melihat, membandingkan, dan memulihkan versi sebelumnya dari proyek.
2. **Branching and Merging**<br>
Git memungkinkan pembuatan cabang (branch) untuk mengerjakan fitur baru atau perbaikan tanpa mengganggu kode utama (master/main). Hal ini sangat mendukung adanya pengembangan paralel. Setelah pekerjaan selesai di cabang, Git memungkinkan penggabungan (merge) cabang tersebut kembali ke cabang utama, menyatukan perubahan dengan cara yang terkelola.
3. **Kolaborasi**<br>
Git adalah sistem terdistribusi, artinya setiap programmer memiliki salinan lengkap dari repositori. Ini memungkinkan kolaborasi tim dengan sinkronisasi yang efisien. Programmer juga dapat mengusulkan perubahan yang harus ditinjau oleh tim sebelum digabungkan ke cabang utama.
4. **Backup and Recovery**<br>
Dengan Git, setiap salinan repositori adalah cadangan dari proyek, mengurangi risiko kehilangan data.
5. **Tracking Changes**<br>
Adanya commit messages memungkinkan para programmer untuk menjelaskan apa yang telah diubah dan mempermudah pelacakan perubahan. Siapa yang membuat perubahan, dan kapan perubahan tersebut dilakukan. Dengan diffs kita bisa mmebandingkan versi file untuk melihat perubahan secara detail
6. **Integrasi dengan Alat lain**<br>
Git dapat diintegrasikan dengan alat CI/CD untuk otomatisasi build, testing, dan deployment. Contoh Integrasi lain adalah IDE. Banyak IDE dan editor yang mendukung integrasi Git, sehingga memudahkan penggunaan langsung

### 4. Kenapa Django Dijadikan Permulaan dalam Pembelajaran Framework?
Django sendiri adalah platform dengan _server-based-application_, menurut yang saya dengar Django sangat bagus di bagian _backend_ nya dan hal ini akan memudahkan kita setelah UTS ketika kita ingin mengakses atau menampilkan data yang disediakan oleh server dengan menggunakan _flutter_
1. **Konsistensi dan Struktur**<br>
Django mengikuti pola desain Model-View-Template (MVT) yang terstruktur, sehingga memudahkan pemahaman alur aplikasi web.<br>
2. **Dokumentasi dan Komunitas**<br>
Django memiliki dokumentasi yang sangat lengkap dan terperinci, yang sangat berguna bagi pemula untuk belajar dan menyelesaikan masalah. Selain itu, Django juga memiliki komunitas yang besar dan aktif serta telah banyak digunakan di dunia industri<br>
3. **Fitur Built-In**<br>
Django menyediakan antarmuka admin yang kuat dan otomatis untuk mengelola data aplikasi tanpa perlu menulis kode tambahan, sangat berguna untuk pemula. Fitur-fitur seperti ORM (Object-Relational Mapping), sistem autentikasi, dan formulir bawaan juga sangat mempermudah pengembangan<br>
4. **Keamanan**<br>
Django menyediakan banyak fitur keamanan bawaan, seperti perlindungan terhadap serangan CSRF, XSS, dan SQL Injection, yang membantu pemula mengembangkan aplikasi yang aman tanpa harus memahami detail keamanan secara mendalam.<br>
5. **Skalabilitas dan Kinerja**<br>
Django dirancang untuk menangani aplikasi web besar dan kompleks, dan bisa dioptimalkan lebih lanjut jika diperlukan. Meskipun cocok untuk aplikasi kecil, Django juga mendukung skala besar, jadi pemula dapat memulai dengan proyek kecil dan berkembang ke aplikasi yang lebih besar seiring waktu.<br>
6. **Pengalaman user dan Pengembangan**<br>
Django menyediakan alat seperti shell interaktif dan server pengembangan bawaan yang mempermudah pengembangan dan pengujian aplikasi. Django juga memiliki dukungan built-in untuk pengujian unit dan integrasi, yang akan membantu pemula untuk menulis dan menjalankan tes aplikasi dengan mudah.<br>
7. **Konsep kerja KISS dan DRY*<br>
Framework telah memenuhi prinsip _KISS (Keep It Short and Simple)_ dan _DRY (Dont Repeat Yourself)_. KISS berarti kode django yang ditulis harus singkat, mudah dimengerti , dan metode yang tidak lebih dari 40-50 baris. Selain itu, django juga mengikuti prinsip DRY, yaitu software pattern yang sering muncul dapat digantikan dengan abstraction sehingga pihak pengembang dapat menyederhanakan proses pengembangan dan membantu mempercepat waktu produksi secara keseluruhan.<br>

### 5. Kenapa Model di Django Disebut ORM?
Model di Django disebut _ORM (Object-Relational Mapping)_ karena ia menyediakan mekanisme yang memungkinkan developer untuk berinteraksi dan bekerja dengan database menggunakan _objek Python_ (paradigma objek) bukan langsung dengan _Query SQL_. Dengan menggunakan model, Anda tidak perlu menulis SQL secara langsung dan manual untuk operasi dasar seperti pembuatan tabel, penyimpanan, pembaruan, dan penghapusan data. Django ORM secara otomatis menangani pembuatan dan pengelolaan tabel database melalui sistem migrasi. _ORM_ juga menyediakan _API_ berbasis objek untuk melakukan operasi query. Alih-alih menulis query SQL, Anda dapat menggunakan metode seperti _.filter(), .get(), dan .exclude()_ pada querysets. ORM memungkinkan kita untuk mendefinisikan relasi antar tabel, dan memudahkan kita dalam mendesain schema database.