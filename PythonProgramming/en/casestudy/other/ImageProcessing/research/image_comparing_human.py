from PIL import Image
import numpy as np
from collections import Counter

# Step 1: Tentukan warna RGB pada Cloth dari gambar parsing

# Load hasil parsing (mask)
mask_img = Image.open("D:/My_Research/gambar2_result.png").convert("RGB")
mask_arr = np.array(mask_img)

# Hitung warna dominan (selain hitam)
pixels = mask_arr.reshape(-1, 3)
pixels = [tuple(p) for p in pixels if not np.all(p == 0)]  # exclude black

# Hitung jumlah tiap warna
color_counts = Counter(pixels)

# Ambil warna dominan (misalnya Top/Baju)
cloth_rgb, _ = color_counts.most_common(1)[0]
print("Cloth RGB Color:", cloth_rgb)



#  Step 2: Ambil semua koordinat pixel dari RGB cloth di parsing, dan gunakan untuk akses Gambar1

# Ambil koordinat mask yang warnanya cloth_rgb
cloth_mask = np.all(mask_arr == cloth_rgb, axis=-1)

# Load Gambar1
original_img = Image.open("D:/My_Research/gambar1.jpg").convert("RGB")
original_arr = np.array(original_img)

# Ambil nilai RGB dari original image di bagian cloth saja
cloth_pixels = original_arr[cloth_mask]



# Step 3: Bandingkan Gambar1 & Gambar2 tapi abaikan area cloth (dari parsing)

# Load Gambar2
image2 = Image.open("D:/My_Research/gambar2_result.jpg").convert("RGB")
image2 = image2.resize(original_img.size)  # samakan ukuran
image2_arr = np.array(image2)

# Buat result array (mulai dari Gambar1)
result = original_arr.copy()

# Bandingkan RGB antar gambar1 dan gambar2
pixel_diff = np.any(original_arr != image2_arr, axis=-1)

# Tapi abaikan pixel yang merupakan cloth (jangan ubah)
apply_black_mask = np.logical_and(pixel_diff, ~cloth_mask)

# Set pixel berbeda (bukan cloth) menjadi hitam
result[apply_black_mask] = [0, 0, 0]

# Simpan hasilnya
output = Image.fromarray(result)
output.save("D:/My_Research/hasil_final.jpg")
print("Saved to hasil_final.jpg")
