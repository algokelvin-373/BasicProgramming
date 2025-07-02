from PIL import Image
import numpy as np
import time

# Load two image
img1 = Image.open("D:/My_Research/gambar1.jpg").convert("RGB")
img2 = Image.open("D:/My_Research/gambar2.jpg").convert("RGB")

# Check size image
if img1.size != img2.size:
    raise ValueError("Ukuran gambar tidak sama!")

# Convert to array numpy
arr1 = np.array(img1)
arr2 = np.array(img2)

# Comparing pixel per pixel (True if has different)
diff_mask = np.any(arr1 != arr2, axis=-1)

# Result: jika beda → hitam, jika sama → ambil dari arr1
result = np.where(diff_mask[..., None], [0, 0, 0], arr1)

# Convert to result image
times = time.time()
output_img = Image.fromarray(result.astype(np.uint8))
output_img.save(f"D:/My_Research/result{times}.jpg")
print("Done")
