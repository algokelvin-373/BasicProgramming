from PIL import Image
import numpy as np
from collections import Counter

# Load result parsing (mask)
mask_img = Image.open("D:/My_Research/gambar2_result.png").convert("RGB")
mask_arr = np.array(mask_img)

# Calculate warna dominate (selain hitam)
pixels = mask_arr.reshape(-1, 3)
pixels = [tuple(p) for p in pixels if not np.all(p == 0)]  # exclude black

# Hitung jumlah tiap warna
color_counts = Counter(pixels)

# Ambil warna dominan (misalnya Top/Baju)
cloth_rgb, _ = color_counts.most_common(1)[0]
print("Cloth RGB Color:", cloth_rgb)
