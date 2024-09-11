# AzkaVogue
AzkaVogue adalah aplikasi web berbasis Django untuk menampilkan produk fashion seperti jaket kulit, jaket jeans, dan celana corduroy. Aplikasi ini menunjukkan produk dengan atribut seperti nama, harga, deskripsi, dan kuantitas.

## Implementasi Checklist
### 1. Membuat Proyek Django Baru
Untuk membuat sebuah folder proyek Django baru, saya menjalankan perintah
*django-admin startproject [myproject]*
Nantinya django akan secara otomatis menyediakan sebuah struktur dasar yang berisi manage.py, folder myproject/, dan berkas konfigurasi utama seperti settings.py, urls.py, dll

### 2. Membuat Aplikasi dengan nama main
Dengan perintah *python manage.py startapp [main]*
Disini saya membuat aplikasi baru di dalam proyek django saya dengan nama 'main'. Folder ini akan berisi berkas utama seperti models.py, views.py, urls.py, dll. Nama aplikasi di Django kita juga bisa disesuaikan dengan kebutuhan proyek, tidak harus main.

### 3. Melakukan Routing pada Proyek untuk Menjalankan Aplikasi main
Agar URL dapat diakses dan terhubung dengan views yang sesuai, kita perlu melakukan routing. Jadi setiap kali pengguna mengunjungi URL tertentu di browser, Django perlu mengetahui bagaimana menangani permintaan tersebut dan apa yang harus ditampilkan
- Buka berkas *myproject/settings.py* dan tambahkan aplikasi main ke dalam *INSTALLED_APPS*. //untuk memberi tahu Django bahwa aplikasi main telah dibuat dan akan digunakan dalam proyek.
- Buat file *main/urls.py* dan tambahkan routing dasar untuk aplikasi main. //Routing ini akan menghubungkan URL tertentu dengan fungsi-fungsi view di dalam aplikasi
- Di *myproject/urls.py*, tambahkan routing untuk aplikasi main //menghubungkannya dengan routing utama proyek, saya mengarkan semua URL yang dimulai dengan main/ ke routing apl main

### 4. Membuat Model Product dengan Atribut name, price, dan description
Model Product dibuat di dalam *main/models.py* untuk mendefinisikan struktur data yang akan disimpan di database. Perintah makemigrations dan migrate diperlukan dalam Django untuk mengaplikasikan perubahan tersebut ke dalam database. 
- *makemigrations* (mendeteksi perubahan, misalkan saya menambahkan quantity, ketika makemigrations dijalankan Django akan membuat file migrasi yang mencatat bahwa tabel produk di database harus menambahkan kolom quantity)
- *migrate* (menjalankan file migrasi yang dihasilkan oleh makemigrations ke dalam database sebenarnya) 

### 5. Membuat Fungsi pada views.py untuk Menampilkan Nama Aplikasi serta Nama dan Kelas Kamu
Di *main/views.py*, saya membuat fungsi *show_main* bertanggung jawab untuk mengumpulkan data yang akan dikirimkan ke template HTML dan kemudian menampilkan template tersebut kepada pengguna, disini saya menampilkan nama aplikasi, nama dan kelas saya

### 6. Membuat Routing pada urls.py Aplikasi main untuk Mepetakan Fungsi di views.py
Seperti yang telah saya jelaskan sebelumnya, misalnya, ketika pengguna mengakses */main/*, fungsi *show_main* akan dieksekusi, dan template *main.html* dengan konteks yang diberikan akan dikirim sebagai respon.

### 7. Melakukan Deployment ke PWS
Setelah aplikasi selesai dan berfungsi dengan baik di lingkungan lokal, deploy ke platform PWS

### 8. Membuat README.md dan Jawaban Pertanyaan
File *README.md* ini mencakup tautan menuju aplikasi PWS yang sudah di-deploy dan jawaban dari beberapa pertanyaan.

## Tautan Aplikasi

## Jawaban Pertanyaan
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?
Saya memulai dengan membuat proyek dan aplikasi di Django, menambahkan model Product, mengatur routing dan views, lalu menambahkan data ke dalam template HTML. Setelah pengembangan selesai di lokal, saya melakukan deployment ke PWS. Penjelasan lebih jelas dapat dilihat pada bagian implementasi checklist
2. Bagan Request dan Response:

3. Fungsi Git dalam Pengembangan Perangkat Lunak:
*a. Version Control*
Git menyimpan riwayat semua perubahan yang dilakukan pada kode, sehingga memungkinkan programmer untuk melihat, membandingkan, dan memulihkan versi sebelumnya dari proyek.
*b. Branching and Merging*
Git memungkinkan pembuatan cabang (branch) untuk mengerjakan fitur baru atau perbaikan tanpa mengganggu kode utama (master/main). Hal ini sangat mendukung adanya pengembangan paralel. Setelah pekerjaan selesai di cabang, Git memungkinkan penggabungan (merge) cabang tersebut kembali ke cabang utama, menyatukan perubahan dengan cara yang terkelola.
*c. Kolaborasi*
Git adalah sistem terdistribusi, artinya setiap programmer memiliki salinan lengkap dari repositori. Ini memungkinkan kolaborasi tim dengan sinkronisasi yang efisien. Programmer juga dapat mengusulkan perubahan yang harus ditinjau oleh tim sebelum digabungkan ke cabang utama.
*d. Backup and Recovery*
Dengan Git, setiap salinan repositori adalah cadangan dari proyek, mengurangi risiko kehilangan data.
*e. Tracking Changes*
Adanya commit messages memungkinkan para programmer untuk menjelaskan apa yang telah diubah dan mempermudah pelacakan perubahan. Siapa yang membuat perubahan, dan kapan perubahan tersebut dilakukan. Dengan diffs kita bisa mmebandingkan versi file untuk melihat perubahan secara detail
*f. Integrasi dengan Alat lain*
CI/CD = Git dapat diintegrasikan dengan alat CI/CD untuk otomatisasi build, testing, dan deployment.
IDE = Banyak IDE dan editor yang mendukung integrasi Git, sehingga memudahkan penggunaan langsung

4. Kenapa Django Dijadikan Permulaan dalam Pembelajaran Framework?
Django sendiri adalah platform dengan *server-based-application*, menurut yang saya dengar Django sangat bagus di bagian backend nya dan hal ini akan memudahkan kita setelah UTS ketika kita ingin mengakses atau menampilkan data yang disediakan oleh server dengan menggunakan flutter  
*1. KONSISTENSI DAN STRUKTUR*
Django mengikuti pola desain Model-View-Template (MVT) yang terstruktur, sehingga memudahkan pemahaman alur aplikasi web.
*2. DOKUMENTASI DAN KOMUNITAS*
Django memiliki dokumentasi yang sangat lengkap dan terperinci, yang sangat berguna bagi pemula untuk belajar dan menyelesaikan masalah. Selain itu, Django juga memiliki komunitas yang besar dan aktif serta telah banyak digunakan di dunia industri
*3. FITUR BUILT-IN*
Django menyediakan antarmuka admin yang kuat dan otomatis untuk mengelola data aplikasi tanpa perlu menulis kode tambahan, sangat berguna untuk pemula. Fitur-fitur seperti ORM (Object-Relational Mapping), sistem autentikasi, dan formulir bawaan juga sangat mempermudah pengembangan
*4. KEAMANAN*
Django menyediakan banyak fitur keamanan bawaan, seperti perlindungan terhadap serangan CSRF, XSS, dan SQL Injection, yang membantu pemula mengembangkan aplikasi yang aman tanpa harus memahami detail keamanan secara mendalam.
*5. SKALABILITAS DAN KINERJA*
Django dirancang untuk menangani aplikasi web besar dan kompleks, dan bisa dioptimalkan lebih lanjut jika diperlukan. Meskipun cocok untuk aplikasi kecil, Django juga mendukung skala besar, jadi pemula dapat memulai dengan proyek kecil dan berkembang ke aplikasi yang lebih besar seiring waktu.
*6. PENGALAMAN USER DAN PENGEMBANGAN*
Django menyediakan alat seperti shell interaktif dan server pengembangan bawaan yang mempermudah pengembangan dan pengujian aplikasi. Django juga memiliki dukungan built-in untuk pengujian unit dan integrasi, yang akan membantu pemula untuk menulis dan menjalankan tes aplikasi dengan mudah.
*7. KONSEP KERJA KISS DAN DRY*
Framework telah memenuhi prinsip KISS (Keep It Short and Simple) dan DRY (Dont Repeat Yourself). KISS berarti kode django yang ditulis harus singkat, mudah dimengerti , dan metode yang tidak lebih dari 40-50 baris. Selain itu, django juga mengikuti prinsip DRY, yaitu software pattern yang sering muncul dapat digantikan dengan abstraction sehingga pihak pengembang dapat menyederhanakan proses pengembangan dan membantu mempercepat waktu produksi secara keseluruhan.

5. Kenapa Model di Django Disebut ORM?
Model di Django disebut ORM (Object-Relational Mapping) karena ia menyediakan mekanisme yang memungkinkan developer untuk berinteraksi dan bekerja dengan database menggunakan objek Python (paradigma objek) bukan langsung dengan Query SQL. Dengan menggunakan model, Anda tidak perlu menulis SQL secara langsung dan manual untuk operasi dasar seperti pembuatan tabel, penyimpanan, pembaruan, dan penghapusan data. Django ORM secara otomatis menangani pembuatan dan pengelolaan tabel database melalui sistem migrasi.

ORM juga menyediakan API berbasis objek untuk melakukan operasi query. Alih-alih menulis query SQL, Anda dapat menggunakan metode seperti .filter(), .get(), dan .exclude() pada querysets. ORM memungkinkan kita untuk mendefinisikan relasi antar tabel, dan memudahkan kita dalam mendesain schema database.