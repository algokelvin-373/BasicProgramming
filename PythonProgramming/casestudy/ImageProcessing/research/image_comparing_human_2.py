from PIL import Image
import numpy as np

# Poin 1: Hilangkan selain area cloth (bersihkan head, leg, dll)

# Load hasil parsing dan original image
mask_img = Image.open("D:/My_Research/gambar2_result.png").convert("RGB")
mask_arr = np.array(mask_img)

original_img = Image.open("D:/My_Research/gambar1.jpg").convert("RGB")
original_arr = np.array(original_img)

# Definisikan cloth_rgb secara eksplisit (atau ambil dari sebelumnya jika masih dalam scope)
cloth_rgb = (128, 0, 128)  # contoh: warna ungu dari parsing

# Buat mask untuk cloth saja
cloth_mask = np.all(mask_arr == cloth_rgb, axis=-1)

# Buat canvas putih
output_white = np.ones_like(original_arr) * 255

# Hanya copy pixel cloth dari original ke canvas putih
output_white[cloth_mask] = original_arr[cloth_mask]

Image.fromarray(output_white).save("D:/My_Research/hasil_cloth_only.jpg")
print("Saved: hasil_cloth_only.jpg")


# Poin 2: Putihkan hasil_final dan salin RGB dari gambar1 ke titik hitam hasil_final

# Load hasil_final dan gambar1
hasil_final = Image.open("D:/My_Research/hasil_final.jpg").convert("RGB")
hasil_arr = np.array(hasil_final)

original_img = Image.open("D:/My_Research/gambar1.jpg").convert("RGB")
original_arr = np.array(original_img)

# Buat canvas putih
white_canvas = np.ones_like(hasil_arr) * 255

# Cari area hitam di hasil_final
black_mask = np.all(hasil_arr == [0, 0, 0], axis=-1)

# Ambil kembali RGB dari original image di lokasi hitam itu
white_canvas[black_mask] = original_arr[black_mask]

# Simpan hasil perbaikan
Image.fromarray(white_canvas).save("D:/My_Research/hasil_final_fixed.jpg")
print("Saved: hasil_final_fixed.jpg")
