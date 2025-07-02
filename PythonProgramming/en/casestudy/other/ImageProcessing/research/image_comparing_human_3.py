from PIL import Image
import numpy as np

# Load semua gambar yang dibutuhkan
original_img = Image.open("D:/My_Research/gambar1.jpg").convert("RGB")
original_arr = np.array(original_img)

gambar2_img = Image.open("D:/My_Research/gambar2_result.jpg").convert("RGB")
gambar2_img = gambar2_img.resize(original_img.size)
gambar2_arr = np.array(gambar2_img)

cloth_mask_img = Image.open("D:/My_Research/hasil_cloth_mask_bw.jpg").convert("RGB")
cloth_mask_arr = np.array(cloth_mask_img)

# Buat mask cloth: pixel putih (255,255,255)
cloth_mask = np.all(cloth_mask_arr == [255, 255, 255], axis=-1)

# Salin pixel dari gambar1 ke gambar2 hanya untuk area cloth
gambar2_arr[cloth_mask] = original_arr[cloth_mask]

# Simpan hasil akhir
Image.fromarray(gambar2_arr).save("D:/My_Research/gambar2_fixed.jpg")
print("Saved: gambar2_fixed.jpg")
