---
# Implementasi Filter Spasial (Spatial Filtering) pada Pengolahan Citra Digital
Project ini merupakan implementasi teknik **Spatial Filtering** untuk memproses citra digital menggunakan bahasa pemrograman Python (OpenCV). Fokus utama dari project ini adalah membandingkan efektivitas Filter Linear dan Non-Linear dalam menangani *noise* serta mendeteksi tepi objek.

## 👥 Anggota Kelompok
Berdasarkan materi presentasi, project ini disusun oleh:
* Faturrahman Ikhsan 
* M. Fatih Amri 
* M. Syauqi Nadhifasla 
* Keisandy Dafa.M 

## 📚 Landasan Teori
### 1. Pengertian Spatial Filtering

Spatial filtering adalah teknik pengolahan citra yang memodifikasi nilai sebuah piksel dengan memanfaatkan informasi dari piksel-piksel di sekitarnya (neighborhood). Proses ini dilakukan pada domain spasial, yang artinya pengolahan dilakukan langsung berdasarkan posisi dan nilai intensitas piksel pada citra.

Tujuan utama dari penerapan spatial filtering adalah:
* Mengurangi *noise* agar citra lebih bersih.
* Menghaluskan citra (*smoothing*) agar visual lebih nyaman.
* Menonjolkan detail atau tepi objek (*edge detection*).


### 2. Konsep Neighborhood dan Konvolusi

Kualitas hasil filter ditentukan oleh **Neighborhood**, yaitu area di sekitar piksel yang digunakan untuk menentukan nilai output. Ukuran neighborhood sangat berpengaruh; semakin luas areanya, efek perubahan makin kuat namun detail halus berpotensi menjadi blur.
Proses penerapannya menggunakan **Konvolusi**, yaitu proses menerapkan kernel (matriks bobot) ke citra secara berulang di seluruh area.

### 3. Jenis Filter

Berdasarkan cara kerjanya, filter dibagi menjadi dua kategori utama:
* **Filter Linear:**
* Output dihitung sebagai gabungan berbobot dari piksel tetangga.
* Contoh: **Mean Filter, Gaussian Filter, Sobel Filter**.
* Aturan penggunaan: Cocok untuk *noise* acak atau *smoothing*.

* **Filter Non-Linear:**
* Output ditentukan oleh aturan non-linear (bukan sekadar penjumlahan), seperti pengurutan nilai.
* Contoh: **Median Filter**.
* Aturan penggunaan: Sangat ampuh untuk *noise* titik (*salt-pepper*) dan menjaga tepi objek.

## 🛠️ Implementasi Kode
Kode program melakukan simulasi dengan menambahkan *Salt & Pepper Noise* pada citra asli, kemudian memperbaikinya menggunakan berbagai metode filter.

### Requirements

* Python 3.x
* OpenCV (`cv2`)
* NumPy (`numpy`)
* Matplotlib (`matplotlib`)

## 📊 Analisis Hasil & Kesimpulan

Berdasarkan hasil visualisasi dari kode program, diperoleh kesimpulan sebagai berikut sesuai dengan teori pemilihan filter:

1. **Penanganan Noise Titik (Salt & Pepper):**
* **Median Filter (Non-Linear)** terbukti paling efektif menghilangkan bintik-bintik noise hingga bersih. Hal ini sesuai teori bahwa noise titik (*salt-pepper*) sebaiknya ditangani dengan median.

* 
**Mean & Gaussian (Linear)** hanya membuat noise menjadi blur/samar, namun tidak hilang sepenuhnya, karena sifatnya yang merata-ratakan nilai piksel.

2. **Smoothing (Penghalusan):**
* **Mean Filter** memberikan efek blur yang cukup kasar.
* **Gaussian Filter** memberikan efek blur yang lebih natural karena memberikan bobot lebih besar pada piksel tengah kernel.

3. **Deteksi Tepi:**
* **Sobel Filter** berhasil mengisolasi garis tepi objek (membuat background menjadi hitam dan garis menjadi putih). Ini sesuai dengan fungsi kernel untuk menonjolkan perubahan atau *sharpen/edge*.

---

*Project ini disusun untuk memenuhi tugas Mata Kuliah Pengolahan Citra Digital.*
