from PIL import Image
import numpy as np

# Load semua gambar
gambar1 = Image.open("D:/My_Research/gambar1.jpg").convert("RGB")
gambar2 = Image.open("D:/My_Research/gambar2_result.jpg").convert("RGB").resize(gambar1.size)
cloth_mask = Image.open("D:/My_Research/hasil_cloth_mask_bw.jpg").convert("RGB").resize(gambar1.size)

# Konversi ke array
arr1 = np.array(gambar1)
arr2 = np.array(gambar2)
mask = np.array(cloth_mask)

# Mask area cloth (putih: [255, 255, 255])
cloth_area = np.all(mask == [255, 255, 255], axis=-1)

# Salin RGB dari Gambar2 ke Gambar1 hanya pada area cloth
arr1[cloth_area] = arr2[cloth_area]

# Simpan hasil akhir
Image.fromarray(arr1).save("D:/My_Research/gambar1_fixed.jpg")
print("Saved: gambar1_fixed.jpg")
