import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Fungsi Pembantu (Helper) untuk Menambahkan Noise ---
# Kita butuh noise supaya efek filter (seperti di Slide 8) terlihat jelas
def add_salt_pepper_noise(image, amount=0.02):
    row, col = image.shape
    s_vs_p = 0.5
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[tuple(coords)] = 255
    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[tuple(coords)] = 0
    return out

# --- 2. Load Citra ---
# Pastikan ganti 'gambar_anda.jpg' dengan nama file gambar yang bos punya
# Kita load sebagai Grayscale agar proses konvolusi lebih mudah dipahami
img_path = 'gambar_anda.jpg' 

# (Untuk contoh kode ini, kita buat gambar dummy jika file tidak ada)
try:
    original_img = cv2.imread(img_path, 0)
    if original_img is None: raise Exception("Gambar tidak ditemukan")
except:
    print("File gambar tidak ditemukan, membuat gambar dummy...")
    original_img = np.zeros((300, 300), dtype=np.uint8)
    cv2.rectangle(original_img, (50, 50), (250, 250), 200, -1)
    cv2.putText(original_img, "Citra Digital", (70, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 0, 2)

# Tambahkan noise (gangguan) untuk simulasi kasus di PDF
noisy_img = add_salt_pepper_noise(original_img)

# --- 3. Implementasi Filter Berdasarkan Slide PDF ---

# A. FILTER LINEAR (Smoothing) [cite: 64, 66]
# Cocok untuk noise acak, tapi bisa membuat blur detail halus.
# 1. Mean Filter (Rata-rata)
mean_kernel_size = (5, 5)
mean_filtered = cv2.blur(noisy_img, mean_kernel_size)

# 2. Gaussian Filter [cite: 66, 73]
# Lebih bagus dari Mean karena memberikan bobot lebih besar pada piksel tengah kernel.
gaussian_filtered = cv2.GaussianBlur(noisy_img, (5, 5), 0)

# B. FILTER NON-LINEAR [cite: 67]
# 3. Median Filter [cite: 70, 74]
# Sangat ampuh untuk noise titik (Salt & Pepper) sambil menjaga tepi objek.
median_filtered = cv2.medianBlur(noisy_img, 5)

# C. EDGE DETECTION (Deteksi Tepi) 
# 4. Sobel Filter
# Sobel menghitung gradien (perubahan intensitas).
sobelx = cv2.Sobel(original_img, cv2.CV_64F, 1, 0, ksize=3) # Gradien arah x
sobely = cv2.Sobel(original_img, cv2.CV_64F, 0, 1, ksize=3) # Gradien arah y
# Menggabungkan gradien x dan y
sobel_combined = cv2.magnitude(sobelx, sobely) 

# --- 4. Menampilkan Hasil (Visualisasi) ---
plt.figure(figsize=(12, 8))

titles = ['Citra Asli (Original)', 'Citra dengan Noise (Salt & Pepper)', 
          'Mean Filter (Linear)', 'Gaussian Filter (Linear)', 
          'Median Filter (Non-Linear)', 'Sobel (Edge Detection)']
images = [original_img, noisy_img, 
          mean_filtered, gaussian_filtered, 
          median_filtered, sobel_combined]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
