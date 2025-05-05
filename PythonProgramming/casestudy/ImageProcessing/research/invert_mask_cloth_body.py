from PIL import Image
import numpy as np

# Load hasil_cloth_only
cloth_img = Image.open("D:/My_Research/hasil_cloth_only.jpg").convert("RGB")
cloth_arr = np.array(cloth_img)

# Mask: area cloth (tidak putih)
cloth_mask = ~np.all(cloth_arr == [255, 255, 255], axis=-1)

# Buat canvas hitam
output = np.zeros_like(cloth_arr)

# Set area cloth menjadi putih
output[cloth_mask] = [255, 255, 255]

# Simpan hasil mask hitam-putih (binary)
Image.fromarray(output).save("D:/My_Research/hasil_cloth_mask_bw.jpg")
print("Saved: hasil_cloth_mask_bw.jpg")
